import os
from langchain_community.vectorstores import FAISS
from app.core.embeddings import get_embedding_model

VECTOR_DB_PATH = "data/faiss_index"


def create_vector_store(chunks: list):
    """
    Create FAISS vector store from chunked documents
    """
    texts = [chunk["text"] for chunk in chunks]
    metadatas = [chunk["metadata"] for chunk in chunks]

    embedding_model = get_embedding_model()

    vector_store = FAISS.from_texts(
        texts=texts,
        embedding=embedding_model,
        metadatas=metadatas
    )

    os.makedirs(VECTOR_DB_PATH, exist_ok=True)
    vector_store.save_local(VECTOR_DB_PATH)

    return vector_store


def load_vector_store():
    """
    Load existing FAISS vector store
    """
    embedding_model = get_embedding_model()

    return FAISS.load_local(
        VECTOR_DB_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )
