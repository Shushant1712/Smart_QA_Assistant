from bs4 import BeautifulSoup


def extract_html(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    for script in soup(["script", "style"]):
        script.decompose()

    text = soup.get_text(separator="\n")

    return [{
        "text": text,
        "metadata": {
            "source": file_path
        }
    }]
