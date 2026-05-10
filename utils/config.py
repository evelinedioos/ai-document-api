import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "AI Document API")
DEBUG = os.getenv("DEBUG", "False") == "True"