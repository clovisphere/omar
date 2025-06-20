import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load environment variables from .env file
load_dotenv()


class Settings(BaseSettings):
    """
    Configuration settings for the application.

    This class consolidates environment variables
    using Pydantic for validation and type safety.
    """

    # --- Core Application Settings ---

    # API version used in routing
    API_VERSION: str = "v1"
    # Root URL for the app (e.g., https://yourapp.com)
    BASE_URL: str = os.getenv("BASE_URL", "")
    # roject name (defaults to 'Omar')
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "Omar")
    # Runtime environment
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    # List of CORS origins allowed to access the API.
    # Defaults to wildcard ('*'), allowing all origins.
    ALLOWED_CORS_ORIGINS: list[str] = os.getenv("ALLOWED_CORS_ORIGINS", "*").split(",")
    # Full Telegram webhook URL based on base and API version
    WEBHOOK_URL: str = f"{BASE_URL}/{API_VERSION}/webhook"

    # --- Gemini Settings ---

    GOOGLE_GENAI_USE_VERTEXAI: bool = bool(os.getenv("GOOGLE_GENAI_USE_VERTEXAI", False))
    # Gemini model to use
    GOOGLE_GENAI_MODEL: str = os.getenv("GOOGLE_GENAI_MODEL", "gemini-2.5-pro")
    # API key for accessing Gemini
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")

    # --- OpenAI Settings ---

    # OpenAI model to use
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "openai/gpt-4o-mini")
    # API key for OpenAI
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")

    # --- Telegram Settings ---

    # Telegram bot token
    TELEGRAM_TOKEN: str = os.getenv("TELEGRAM_TOKEN", "")
    # Read timeout for Telegram API
    TELEGRAM_READ_TIMEOUT: float = float(os.getenv("TELEGRAM_READ_TIMEOUT", 5.0))

    # Informative message to help users interact with Omar
    TELEGRAM_HELP_COMMAND: str = """
    \nHere's how you can interact with me:

    /start – Begin your journey with a warm welcome
    /help  – Show this help message \

    \nSimply type your question or reflection, and I'll do my best to guide you.
    """


# Create and expose a global settings instance
settings = Settings()
