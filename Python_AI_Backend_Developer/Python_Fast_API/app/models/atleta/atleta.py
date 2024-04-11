from uuid import UUID
from mongoengine import StringField, IntField, FloatField, UUIDField, DateField, ReferenceField
from categoria.categoria import CategoriaModel
from app.contrib.models import BaseModel
from centro_treinamento.centro_treinamento import CentroTreinamentoModel

class AtletaModel(BaseModel):
    pk_id = UUIDField(primary_key=True)
    nome = StringField(max_length=50, required=True, unique=True, description='Nome do Atleta')
    idade = IntField(required=True, description='Nome do Atleta')
    peso = FloatField(required=True, description='Peso do Atleta')
    altura = FloatField(required=True, description='Altura do Atleta')
    sexo = StringField(required=True, description='Sexo do Atleta')
    categoria = ReferenceField(CategoriaModel)
    centro_treinamento = ReferenceField(CentroTreinamentoModel)
    created_at = DateField(required=True, description='Data de criação')

