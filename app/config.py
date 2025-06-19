import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load environment variables from .env file
load_dotenv()


class Settings(BaseSettings):
    """
    Configuration settings for the application.

    This class consolidates settings from environment variables, providing
    a structured and type-safe way to access configuration values.
    """

    # --- Core Application Settings ---

    # Defaults to 'Ekumen Assistant'.
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "Preacher")

    # --- Gemini Settings ---

    GOOGLE_GENAI_USE_VERTEXAI: bool = bool(os.getenv("GOOGLE_GENAI_USE_VERTEXAI", False))
    GOOGLE_GENAI_MODEL: str = os.getenv("GOOGLE_GENAI_MODEL", "gemini-2.0-flash-001")
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")

    # --- Openai Settings ---

    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "openai/gpt-4o-mini")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")


# Instantiate the settings object, loading values from environment variables.
settings = Settings()
