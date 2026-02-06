
# Smart_QA_Assistant
A GenAI-powered document intelligence system using RAG, FastAPI, Django, and FAISS.
=======
# 📘 Smart Assistant for Summarization

A **GenAI-powered document intelligence system** that enables users to upload large documents and interact with them using **question answering and document-level summarization** powered by **Retrieval-Augmented Generation (RAG)**.

---

## 🚀 Project Overview

Reading long documents such as **research papers, legal files, or technical manuals** is time-consuming. Traditional search and summarization tools fail to provide deep understanding.

This project builds a **Smart Assistant** that:
- Understands uploaded documents
- Answers questions based on document content
- Generates long, clear summaries on demand
- Avoids hallucinations by grounding responses in source text

---

## ✨ Key Features

- 📂 Multi-format document upload (PDF, DOCX, PPTX, CSV, XLSX, MD, HTML)
- 🧠 Retrieval-Augmented Generation (RAG)
- ❓ Question Answering with document context
- 📝 Long, detailed document summaries (user-triggered)
- 🎨 Django-based interactive UI
- ⚡ FastAPI backend
- 🔍 FAISS vector database for semantic search

---

## 🧩 Tech Stack

### Backend
- Python
- FastAPI
- LangChain
- FAISS
- OpenAI API
- Uvicorn

### Frontend
- Django
- HTML / CSS

---

## 📁 Project Structure

## System Architecture

User
 │
 │ Upload Document / Ask Question / Generate Summary
 ▼
Django Frontend (UI)
 │
 │ HTTP Requests
 ▼
FastAPI Backend
 │
 │ Document Ingestion
 │   ├─ Extract text
 │   ├─ Chunk document
 │   ├─ Generate embeddings
 │   └─ Store in FAISS
 │
 │ RAG Pipeline
 │   ├─ Retrieve relevant chunks
 │   ├─ Generate answer / summary
 │   └─ Return response
 ▼
User Interface



/*
!SECTIONsmart-assistant-for-research-summarization/
│
├── backend/                                  # Backend service
│   ├── app/                                 # FastAPI application
│   │   ├── main.py                          # FastAPI entry point
│   │   ├── config.py                        # Environment & app configuration
│   │
│   │   ├── api/                             # API route handlers
│   │   │   ├── upload.py                   # Document upload & validation APIs
│   │   │   ├── qa.py                       # Question answering APIs
│   │   │   └── logic.py                    # Logic-based Q&A & evaluation APIs
│   │   │
│   │   ├── core/                            # Core RAG logic
│   │   │   ├── extractors/                 # File format text extractors
│   │   │   │   ├── pdf_extractor.py        # Extract text + pages from PDF
│   │   │   │   ├── docx_extractor.py       # Extract text from DOCX
│   │   │   │   ├── pptx_extractor.py       # Extract slide-wise text from PPTX
│   │   │   │   ├── csv_extractor.py        # Extract tabular text from CSV
│   │   │   │   ├── xlsx_extractor.py       # Extract sheet-wise text from XLSX
│   │   │   │   ├── md_extractor.py         # Extract text from Markdown
│   │   │   │   └── html_extractor.py       # Extract structured text from HTML
│   │   │   │
│   │   │   ├── loader.py                   # Route files to correct extractor
│   │   │   ├── chunker.py                  # Split text into semantic chunks
│   │   │   ├── embeddings.py               # Generate embeddings for chunks
│   │   │   ├── vectorstore.py              # Store & manage FAISS index
│   │   │   ├── retriever.py                # Retrieve relevant chunks
│   │   │   ├── llm.py                      # OpenAI LLM configuration
│   │   │   └── prompts.py                  # Prompt templates for RAG & logic
│   │   │
│   │   ├── services/                       # Business logic orchestration
│   │   │   ├── ingestion_service.py        # End-to-end document ingestion flow
│   │   │   ├── qa_service.py               # QA workflow orchestration
│   │   │   └── logic_service.py            # Logic question & evaluation workflow
│   │   │
│   │   ├── models/                         # Request/response data models
│   │   │   └── schemas.py                  # Pydantic schemas
│   │   │
│   │   ├── utils/                          # Helper utilities
│   │   │   ├── references.py               # Source citation & justification logic
│   │   │   └── file_utils.py               # File save, cleanup, validation helpers
│   │
│   ├── data/                               # Runtime data storage
│   │   ├── documents/                     # Uploaded documents
│   │   ├── processed/                     # Cleaned & chunked text
│   │   └── faiss_index/                   # FAISS vector database
│   │
│   ├── requirements.txt                   # Backend Python dependencies
│   ├── .env                               # Environment variables
│   └── README.md                          # Backend documentation
│
├── frontend/                               # Frontend application
│   └── django_app/                        # Django-based UI
│       ├── manage.py                      # Django entry point
│       ├── requirements.txt               # Frontend Python dependencies
│       ├── frontend/                      # Django project config
│       │   ├── settings.py                # Django settings
│       │   ├── urls.py                    # URL routing
│       │   └── views.py                   # UI request handling
│       ├── templates/                     # HTML templates
│       │   ├── upload.html                # Document upload UI
│       │   └── chat.html                  # Q&A chat interface
│       └── static/
│           └── css/
│               └── style.css              # UI styling
│
├── docs/                                   # Project documentation
│   ├── architecture.png                   # System architecture diagram
│   └── api_flow.md                        # API flow explanation
│
├── .gitignore                              # Git ignored files
├── README.md                               # Project overview
└── LICENSE                                 # License
*/
