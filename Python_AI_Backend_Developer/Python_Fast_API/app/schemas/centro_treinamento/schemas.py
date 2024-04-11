from pydantic import Field
from app.contrib.schemas import BaseSchema

class CentroTreinamento(BaseSchema):
    nome: str = Field(..., max_length=20, description='Nome da Centro de Treinamento', example='CT KING')
    endereco: str = Field(..., max_length=60, description='Endereço do Centro de Treinamento', example='Rua x, 98')
    proprietario: str = Field(..., max_length=30, description='Proprietárop Centro de Treinamento', example='Pedro')
