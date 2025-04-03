import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("DB_USER")
password = quote_plus(os.getenv("DB_PASSWORD"))  # URL 인코딩
host = os.getenv("DB_HOST")
dbname = os.getenv("DB_NAME")

class Config:
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{user}:{password}@{host}/{dbname}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False