from app.contrib.schemas import BaseSchema, OutMinix
from pydantic import  UUID4, Field, PositiveFloat
from uuid import UUID, uuid4

class Atleta(BaseSchema):
    id: UUID4 = Field(..., default_factory=uuid4)
    nome: str = Field(..., max_length=50, description='Nome do Atleta', example='João')
    cpf: str = Field(..., max_length=11, description='CPF do Atleta', example='11111111111')
    idade: int = Field(..., description='Idade do Atleta', example=24)
    peso: PositiveFloat = Field(..., description='Peso do Atleta', example=65.5)
    altura: PositiveFloat = Field(..., description='Altura do Atleta', example=1.78)
    sexo: str = Field(..., description='Sexo do Atleta', example='M', max_length=1)
    centro_treinamento: str
    categoria_id: UUID


class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMinix):
    pass