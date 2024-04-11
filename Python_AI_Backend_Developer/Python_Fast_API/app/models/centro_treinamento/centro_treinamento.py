from uuid import UUID
from mongoengine import StringField, UUIDField, ReferenceField
from app.contrib.models import BaseModel
from atleta.atleta import AtletaModel

class CentroTreinamentoModel(BaseModel):
    pk_id = UUIDField(primary_key=True)
    nome = StringField(max_length=20, unique=True, required=True, description='Nome do Atleta')
    propritario = StringField(max_length=60, required=True, description='Nome do Atleta')
    endereco = StringField(max_length=30, required=True, description='Nome do Atleta')
    atleta = ReferenceField(AtletaModel)