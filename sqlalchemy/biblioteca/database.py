import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
database = os.getenv("DB_NAME")


db_server = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}")

with db_server.connect() as connection:
    connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {database}"))

db = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")

Session = sessionmaker(bind=db)
session = Session()