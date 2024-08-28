import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

debug_ok = os.getenv("DEBUG")
env = os.getenv("ENV")
access_token = os.getenv("TOKEN")
