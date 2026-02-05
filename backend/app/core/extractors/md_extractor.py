import markdown
from bs4 import BeautifulSoup


def extract_md(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    html = markdown.markdown(md_content)
    soup = BeautifulSoup(html, "html.parser")

    text = soup.get_text(separator="\n")

    return [{
        "text": text,
        "metadata": {
            "source": file_path
        }
    }]
