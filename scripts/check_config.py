import os
from dotenv import load_dotenv

load_dotenv()

database_url = os.environ.get("DATABASE_URL")

if database_url:
    print("DATABASE_URL is configured")
else:
    print("DATABASE_URL is not set")