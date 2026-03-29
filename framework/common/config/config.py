from dotenv import load_dotenv
from pathlib import Path
import os

# Set BASE_DIR to project root
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent  # adjust according to your folder depth

def load_env():
    # Only take one ENV value, default to "local"
    env = os.getenv("ENV", "local")

    # Use absolute paths so .env is always found
    if env == "staging":
        load_dotenv(BASE_DIR / ".env.staging")
    elif env == "prod":
        load_dotenv(BASE_DIR / ".env.prod")
    else:
        load_dotenv(BASE_DIR / ".env")

# Load environment variables
load_env()

class Config:
    BASE_URL = os.getenv("BASE_URL")
    API_BASE_URL = os.getenv("API_BASE_URL")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"