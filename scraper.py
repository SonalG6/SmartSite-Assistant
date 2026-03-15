import os
from dotenv import load_dotenv
from firecrawl import FirecrawlApp

# Load environment variables from .env file
load_dotenv()


class WebsiteScraper:
    def __init__(self):
        api_key = os.getenv("FIRECRAWL_API_KEY")
        if not api_key:
            raise ValueError("FIRECRAWL_API_KEY not found. Please set it in the .env file.")
        self.app = FirecrawlApp(api_key=api_key)

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


if __name__ == "__main__":
    scraper = WebsiteScraper()

    url = input("Enter website URL: ")

    content = scraper.scrape_website(url)

    if content:
        print("Scraping successful!")
        print("Total characters scraped:", len(content))
        print(content[:1000])  # preview first 1000 characters
    else:
        print("Failed to scrape website")
