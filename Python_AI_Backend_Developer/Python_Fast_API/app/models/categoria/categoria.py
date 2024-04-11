from uuid import UUID
from mongoengine import StringField, UUIDField, ReferenceField
from app.contrib.models import BaseModel
from atleta.atleta import AtletaModel

class CategoriaModel(BaseModel):
    pk_id = UUIDField(primary_key=True)
    nome = StringField(max_length=10, unique=True, required=True, description='Nome da Categoria')
    atleta = ReferenceField(AtletaModel)