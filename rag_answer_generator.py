import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


class RAGAnswerGenerator:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env")

        self.client = genai.Client(api_key=api_key)

    def generate_answer(self, question, retrieved_docs):

        context = "\n\n".join(
            [doc["content"] for doc in retrieved_docs]
        )

        prompt = f"""
You are an AI assistant that answers questions using website content.

Only use the information provided in the context.

Context:
{context}

Question:
{question}

Answer clearly and concisely.
"""

        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text