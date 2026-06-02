import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "AI Document API")
DEBUG = os.getenv("DEBUG", "False") == "True"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")