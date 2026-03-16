from scrapper import WebsiteScraper
from document_processor import DocumentProcessor
from vector_store import VectorStore
from rag_answer_generator import RAGAnswerGenerator


scraper = WebsiteScraper()
processor = DocumentProcessor()
vector_store = VectorStore()
rag = RAGAnswerGenerator()

url = input("Enter website URL: ")

docs = scraper.crawl_website(url)

chunks = processor.process_documents(docs)

vector_store.build_vector_store(chunks)

while True:
    try:
        question = input("\nAsk a question about the website: ")
    except EOFError:
        print("\nInput stream ended. Exiting.")
        break

    if not question.strip() or question.strip().lower() in {"exit", "quit"}:
        print("Exiting.")
        break

    retrieved_docs = vector_store.search(question)

    answer = rag.generate_answer(question, retrieved_docs)

    print("\nAnswer:\n")
    print(answer)