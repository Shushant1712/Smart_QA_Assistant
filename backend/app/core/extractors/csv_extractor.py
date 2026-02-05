import pandas as pd


def extract_csv(file_path: str):
    df = pd.read_csv(file_path)

    text = df.astype(str).to_string(index=False)

    return [{
        "text": text,
        "metadata": {
            "source": file_path
        }
    }]
