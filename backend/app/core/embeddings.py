from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

# Ensure env variables are loaded in all execution modes
load_dotenv()


def get_embedding_model():
    return OpenAIEmbeddings()
