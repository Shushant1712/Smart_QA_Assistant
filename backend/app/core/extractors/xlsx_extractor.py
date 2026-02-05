import pandas as pd


def extract_xlsx(file_path: str):
    sheets = pd.read_excel(file_path, sheet_name=None)
    extracted_data = []

    for sheet_name, df in sheets.items():
        text = df.astype(str).to_string(index=False)

        extracted_data.append({
            "text": text,
            "metadata": {
                "sheet": sheet_name,
                "source": file_path
            }
        })

    return extracted_data
