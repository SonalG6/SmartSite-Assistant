import os
import requests
from dotenv import load_dotenv

load_dotenv()


class RAGAnswerGenerator:

    def __init__(self):

        api_key = os.getenv("OPENROUTER_API_KEY")

        if not api_key:
            raise ValueError("OPENROUTER_API_KEY not found in .env")

        self.api_key = api_key
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"

        self.model = os.getenv(
            "OPENROUTER_MODEL",
            "openrouter/auto"
        )

    def generate_answer(self, question, retrieved_docs):

        context = "\n\n".join(
            [doc["content"][:800] for doc in retrieved_docs]
        )

        prompt = f"""
You are an AI assistant answering questions based on website content.

Use ONLY the information provided in the context.
    Always answer in English.

Context:
{context}

Question:
{question}

Answer clearly and concisely.
"""

        response = requests.post(
            self.api_url,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": self.model,
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            },
            timeout=60
        )

        if not response.ok:
            error_text = response.text.strip()
            raise RuntimeError(
                f"OpenRouter API request failed ({response.status_code}): {error_text}"
            )
        data = response.json()
        return data["choices"][0]["message"]["content"]