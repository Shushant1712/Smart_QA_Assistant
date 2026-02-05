from docx import Document


def extract_docx(file_path: str):
    document = Document(file_path)
    extracted_data = []

    for idx, paragraph in enumerate(document.paragraphs):
        text = paragraph.text.strip()
        if text:
            extracted_data.append({
                "text": text,
                "metadata": {
                    "paragraph": idx,
                    "source": file_path
                }
            })

    return extracted_data
