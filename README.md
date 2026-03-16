# SmartSite Assistant

SmartSite Assistant is an RAG-based AI-powered system that converts any website into an interactive knowledge base. By providing a website URL, the system crawls relevant pages, extracts both structured and unstructured content, and enables users to ask natural language questions about the website.

The project implements a Retrieval-Augmented Generation (RAG) pipeline to retrieve relevant information from the website and generate accurate responses grounded in the site's content while ensuring minimal latency.

## Architecture Diagram

```mermaid
flowchart TD
    A[User Input: Website URL] --> B[Website Crawling - Firecrawl]
    B --> C[Content Extraction]
    C --> D[Document Processing & Chunking]
    D --> E[Embedding Generation - Sentence Transformers]
    E --> F[Vector Database - FAISS]
    F --> G[Semantic Retrieval]
    G --> H[LLM Answer Generation]
    H --> I[Final Response to User]

    
## Tech Stack

- **Python** – Core programming language  
- **Firecrawl** – Website crawling and content extraction  
- **LangChain** – RAG pipeline orchestration  
- **FAISS** – Vector database for semantic search  
- **Groq** – LLM for response generation  
- **Streamlit** – Interactive user interface  

## Key Features

- Accepts any website URL as input
- Automatically crawls and processes relevant pages
- Handles both structured and unstructured website content
- Uses semantic search for accurate information retrieval
- Generates context-aware answers using Retrieval-Augmented Generation
- Designed for efficient querying with minimal latency

## Module Descriptions

### scraper.py
Handles website ingestion using Firecrawl.  
It crawls multiple pages from a website and extracts textual content.

### document_processor.py
Processes scraped content and splits it into smaller semantic chunks.

### vector_store.py
Creates embeddings using Sentence Transformers and stores them in a FAISS vector database.

### rag_answer_generator.py
Uses a Large Language Model to generate answers based on retrieved website context.

### test.py
Runs the complete pipeline and integrates all modules.


## Setup Instructions

Clone the repository:

git clone https://github.com/YOUR_USERNAME/SmartSite-Assistant.git

cd SmartSite-Assistant


Create a virtual environment:

python -m venv venv

Activate environment (Windows):

venv\Scripts\activate

Activate environment (Mac/Linux):

source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


## Environment Variables

Create a `.env` file in the root directory.

Example:

FIRECRAWL_API_KEY=your_firecrawl_api_key

LLM_API_KEY=your_llm_api_key


## Running the Project

Run the main script:

python test.py

Example usage:

Enter website URL: https://example.com

Ask a question about the website:

What services does this company offer?
The system will retrieve relevant website content and generate an answer.


## Solution Approach

The system was developed in a modular pipeline:

1. Implement website crawling using Firecrawl.
2. Process scraped website data into smaller chunks.
3. Convert chunks into embeddings.
4. Store embeddings in a FAISS vector database.
5. Retrieve the most relevant chunks based on a query.
6. Use a large language model to generate answers.

This approach ensures accurate responses while maintaining efficient retrieval.

## Note on LLM Integration

The project includes an LLM-based answer generation module as part of the Retrieval-Augmented Generation (RAG) pipeline. 

During testing, API quota limitations were encountered with the initial Gemini integration, which resulted in `RESOURCE_EXHAUSTED (429)` errors during response generation. The architecture was adapted to support Groq's LLaMA-3 model for answer generation.

Due to time constraints before submission, the LLM response generation step may not execute successfully without a valid API quota. However, the complete RAG pipeline — including website crawling, document processing, embedding generation, vector database indexing, and semantic retrieval — is fully implemented and functional.
