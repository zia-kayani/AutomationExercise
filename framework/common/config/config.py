from dotenv import load_dotenv
import os 

def load_env():
    env = os.getenv("ENV" , "local")

    if env == "staging":
        load_dotenv(".env.staging")
    elif env == "prod":
        load_dotenv(".env.prod")
    
    else:
        load_dotenv(".env")

load_env()

class Config:
    BASE_URL =  os.getenv("BASE_URL")
    API_BASE_URL = os.getenv("API_BASE_URL")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"


#to pass in the terminal
#  $env:ENV="prod" 