Name: Utkrisht Agrawal
Email ID: www.rkayush412@gmail.com

📚 GA03: Research Paper Management & Analysis Intelligence System

An end-to-end AI-powered research assistant that enables users to upload academic papers (PDFs) and interact with them using semantic search and Retrieval-Augmented Generation (RAG).

🚀 Key Features

📄 Upload and parse research paper PDFs

✂️ Intelligent chunking with reference-section removal

🧠 Semantic search using FAISS vector indexing

🤖 Context-aware Q&A using Groq-hosted LLaMA 3.1 models

🎯 Strictly grounded answers (anti-hallucination prompts)

🖥️ Researcher-friendly UI built with Streamlit

🧠 Architecture Overview

PDF Upload via Streamlit

Text Extraction using pypdf

Chunking + Overlap, excluding references

Embedding Generation using SentenceTransformers

Vector Indexing with FAISS

Semantic Retrieval for user questions

LLM Answer Generation using Groq (LLaMA 3.1)

🛠️ Tech Stack

Frontend: Streamlit

LLM: Groq (LLaMA 3.1)

Embeddings: SentenceTransformers

Vector Store: FAISS

Language: Python

▶️ Run Locally

git clone https://github.com/Utkrisht9519/GA03-Research-Paper-Assistant.git

cd GA03-Research-Paper-Assistant

pip install -r requirements.txt

streamlit run app.py

Create .streamlit/secrets.toml:

GROQ_API_KEY = "groq_api_key"

💡 Example Questions

1. What problem does this paper address?

2. What methodology is proposed?

3. How does this approach differ from prior work?

4. What are the main contributions?

📈 Learning Outcomes

Built a full RAG pipeline for long technical documents

Implemented semantic retrieval with FAISS

Integrated external LLM APIs securely

Designed a production-style AI research tool

🔮 Future Enhancements

Multi-paper comparison
Automatic structured summaries
Citation graph visualization
Research trend analysis
