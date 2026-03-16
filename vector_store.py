import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


class VectorStore:

    def __init__(self):

        # Load embedding model
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = None
        self.documents = []

    def create_embeddings(self, chunks):
       #Convert text chunks into embeddings

        texts = [doc["content"] for doc in chunks]

        embeddings = self.model.encode(texts)

        return np.array(embeddings)

    def build_vector_store(self, chunks):
       #Build FAISS vector database

        embeddings = self.create_embeddings(chunks)

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(embeddings)

        self.documents = chunks

        print("Vector database built successfully.")
        print("Total vectors stored:", self.index.ntotal)

    def search(self, query, top_k=3):
       #Search similar chunks based on query

        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(query_embedding, top_k)
        results = []

        for idx in indices[0]:
            results.append(self.documents[idx])

        return results
