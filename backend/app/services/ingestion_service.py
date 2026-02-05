from app.core.loader import load_document
from app.core.chunker import chunk_documents
from app.core.vectorstore import create_vector_store


def ingest_document(file_path: str):
    """
    Full ingestion pipeline:
    File → Text extraction → Chunking → Embeddings → FAISS
    """

    # 1. Extract text from document
    extracted_data = load_document(file_path)

    # 2. Chunk the extracted text
    chunked_data = chunk_documents(extracted_data)

    # 3. Create / update FAISS vector store
    create_vector_store(chunked_data)

    # 4. Return only status (no summary here)
    return {
        "message": "Document ingested successfully",
        "total_chunks": len(chunked_data)
    }
