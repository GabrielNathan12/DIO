import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import Field
from pydantic_settings import BaseSettings
from pymongo import MongoClient

load_dotenv()

MONGO_URL = os.getenv('MONGO_URL')
DB_NAME = os.getenv('DB_NAME')

client = MongoClient(MONGO_URL)

db_name = DB_NAME
db = client[db_name]

colecoes = ['atletas', 'categorias', 'centros_treinamento']

for colecao in colecoes:
    if colecao not in db.list_collection_names():
        db.create_collection(colecao)

print("Banco de dados e coleções criados com sucesso!")

class Settings(BaseSettings):
    MONGODB_URL: str = Field(default=MONGO_URL)
    MONGODB_DB_NAME: str = Field(default=DB_NAME)

settings = Settings()

client = AsyncIOMotorClient(settings.MONGODB_URL)
database = client[settings.MONGODB_DB_NAME]