<<<<<<< HEAD
# Smart_Assistant
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
