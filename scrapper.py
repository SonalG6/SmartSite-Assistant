import os
from dotenv import load_dotenv
from firecrawl import FirecrawlApp

# Load environment variables from .env file
load_dotenv()


class WebsiteScraper:
    def __init__(self, api_key=None, max_pages=5):
        if api_key is None:
            api_key = os.getenv("FIRECRAWL_API_KEY")
        if not api_key:
            raise ValueError("FIRECRAWL_API_KEY not found. Please set it in the .env file.")
        self.app = FirecrawlApp(api_key=api_key)
        self.max_pages = max_pages

    def scrape_website(self, url):
        # calls the firecrawl API to scrape the website and extract content in markdown format
        result = self.app.scrape(url, formats=["markdown"])

        if result is None:
            return None
        
        # Support both dict-like and object-like response formats.
        if isinstance(result, dict):
            if "markdown" in result and result["markdown"]:
                return result["markdown"]
            if "data" in result and isinstance(result["data"], dict):
                data = result["data"]
                if "markdown" in data and data["markdown"]:
                    return data["markdown"]
                if "content" in data and data["content"]:
                    return data["content"]
        else:
            markdown = getattr(result, "markdown", None)
            if markdown:
                return markdown
            content = getattr(result, "content", None)
            if content:
                return content

        return None
    
    def crawl_website(self, url):
        try:
            result = self.app.crawl(url, limit=self.max_pages)

            # Firecrawl can return either dict-like payloads or CrawlJob objects.
            pages = result.get("data", []) if isinstance(result, dict) else getattr(result, "data", [])
            documents = []

            for page in pages:
                if isinstance(page, dict):
                    metadata = page.get("metadata", {}) or {}
                    source = metadata.get("sourceURL") or metadata.get("source_url") or metadata.get("url") or page.get("url")
                    content = page.get("markdown") or page.get("content")
                else:
                    metadata = getattr(page, "metadata", None)
                    source = None
                    if metadata is not None:
                        source = getattr(metadata, "source_url", None) or getattr(metadata, "url", None)
                    content = getattr(page, "markdown", None) or getattr(page, "content", None)

                if content:
                    documents.append({
                        "source": source,
                        "content": content,
                    })

            return documents

        except Exception as e:
            print("Crawling failed:", e)
            return []
        


if __name__ == "__main__":
    scraper = WebsiteScraper()

    url = input("Enter website URL: ").strip()

    print("Building knowledge base from website...")

    documents = scraper.crawl_website(url)

    if not documents:
        print("Crawl failed, falling back to single-page scrape.")
        content = scraper.scrape_website(url)

        if content:
            documents = [{"source": url, "content": content}]
        else:
            print("Failed to retrieve content.")
            exit()

    print("Website ingestion complete.")
    print("Total documents collected:", len(documents))

    print("\nSample document preview:\n")
    print(documents[0]["content"][:1000])
