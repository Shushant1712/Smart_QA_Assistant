from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_documents(
    extracted_data: list,
    chunk_size: int = 800,
    chunk_overlap: int = 100
):
    """
    Split extracted document text into semantic chunks
    while preserving metadata for explainability.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    all_chunks = []

    for item in extracted_data:
        text = item["text"]
        metadata = item["metadata"]

        chunks = text_splitter.split_text(text)

        for idx, chunk in enumerate(chunks):
            all_chunks.append({
                "text": chunk,
                "metadata": {
                    **metadata,
                    "chunk_id": idx
                }
            })

    return all_chunks
