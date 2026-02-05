from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def get_llm():
    """
    Initialize OpenAI chat model for QA
    """
    return ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    )
