import os

from dotenv import load_dotenv

# .env ファイルをロードして環境変数へ反映
load_dotenv()

DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')

