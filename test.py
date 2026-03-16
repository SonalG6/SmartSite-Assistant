from scrapper import WebsiteScraper
from document_processor import DocumentProcessor
from vector_store import VectorStore

scraper = WebsiteScraper()
processor = DocumentProcessor()
vector_store = VectorStore()

url = input("Enter website URL: ")

docs = scraper.crawl_website(url)

chunks = processor.process_documents(docs)

vector_store.build_vector_store(chunks)

query = input("Ask a question about the website: ")

results = vector_store.search(query)

print("\nRelevant results:\n")

for r in results:
    print("Source:", r["source"])
    print(r["content"][:300])
    print()
