from dotenv import load_dotenv
from pathlib import Path
import os

# Set BASE_DIR to project root
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent  

def load_env():
    env = os.getenv("ENV", "local")

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