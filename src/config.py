import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")
APP_ENV = os.getenv("APP_ENV", "development")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

if not OPENAI_API_KEY:
    raise RuntimeError(
        "OPENAI_API_KEY environment variable is not configured."
    )

if not OPENAI_MODEL:
    raise RuntimeError(
        "OPENAI_MODEL environment variable is not configured."
    )