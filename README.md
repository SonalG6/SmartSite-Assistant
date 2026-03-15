# SmartSite Assistant

SmartSite Assistant is an RAG-based AI-powered system that converts any website into an interactive knowledge base. By providing a website URL, the system crawls relevant pages, extracts both structured and unstructured content, and enables users to ask natural language questions about the website.

The project implements a Retrieval-Augmented Generation (RAG) pipeline to retrieve relevant information from the website and generate accurate responses grounded in the site's content while ensuring minimal latency.

## Architecture

The system processes a website and builds a knowledge base using the following pipeline:

User Input (Website URL)
        ↓
Website Crawling (Firecrawl)
        ↓
Content Extraction and Cleaning
        ↓
Text Chunking
        ↓
Embedding Generation
        ↓
Vector Storage (FAISS)
        ↓
Semantic Retrieval
        ↓
LLM Response Generation (Google Gemini)
        ↓
Streamlit Chat Interface

## Tech Stack

- **Python** – Core programming language  
- **Firecrawl** – Website crawling and content extraction  
- **LangChain** – RAG pipeline orchestration  
- **FAISS** – Vector database for semantic search  
- **Google Gemini** – LLM for response generation  
- **Streamlit** – Interactive user interface  

## Key Features

- Accepts any website URL as input
- Automatically crawls and processes relevant pages
- Handles both structured and unstructured website content
- Uses semantic search for accurate information retrieval
- Generates context-aware answers using Retrieval-Augmented Generation
- Designed for efficient querying with minimal latency
