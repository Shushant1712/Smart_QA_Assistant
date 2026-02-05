from pypdf import PdfReader


def extract_pdf(file_path: str):
    reader = PdfReader(file_path)

    extracted_data = []

    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if text:
            extracted_data.append({
                "text": text,
                "metadata": {
                    "page": page_num,
                    "source": file_path
                }
            })

    return extracted_data
