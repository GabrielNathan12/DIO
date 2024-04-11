from app.contrib.schemas import BaseSquema
from typing import Annotated
from pydantic import Field,UUID4
class CentroTreinamento(BaseSquema):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', example='CT King', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do Centro de Treinamento', example='RUA X, Q002', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietário do Centro de Treinamento', example='Pedro', max_length=30)]
    
class CentroTreinamentoAtleta(BaseSquema):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', example='CT King', max_length=20)]

class CentroTreinamentoOut(CentroTreinamento):
    id: Annotated[UUID4, Field(description='Identificador do Centro de Treinamento')]
