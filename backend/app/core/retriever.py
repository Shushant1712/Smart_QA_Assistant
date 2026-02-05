from app.core.vectorstore import load_vector_store


def retrieve_relevant_chunks(
    query: str,
    top_k: int = 4
):
    """
    Retrieve top-k semantically relevant chunks for a query
    using FAISS similarity search.
    """
    vector_store = load_vector_store()

    # similarity_search returns Document objects
    results = vector_store.similarity_search(query, k=top_k)

    retrieved_chunks = []

    for doc in results:
        retrieved_chunks.append({
            "text": doc.page_content,
            "metadata": doc.metadata
        })

    return retrieved_chunks
