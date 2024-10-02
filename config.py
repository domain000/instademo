import os

# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

class Config:
    DB_URL = os.getenv('DB_URL')
    DATABASE_NAME = os.getenv('DATABASE_NAME')
    C_N = os.getenv('C_N')
    S_KEY = os.getenv('S_KEY')

    