import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


class Settings:
    # OpenAI
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

    # App settings
    APP_NAME: str = "Smart Assistant for Research Summarization"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True


# Create a single settings object
settings = Settings()
