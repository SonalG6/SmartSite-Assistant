from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentProcessor:

    def __init__(self, chunk_size=500, chunk_overlap=50):

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def process_documents(self, documents):
        #Splits scraped documents into smaller chunks
        processed_docs = []

        for doc in documents:

            content = doc.get("content", "")
            source = doc.get("source", "unknown")

            chunks = self.text_splitter.split_text(content)

            for chunk in chunks:
                processed_docs.append({
                    "source": source,
                    "content": chunk
                })

        return processed_docs
