from typing import Annotated, Optional
from pydantic import Field, PositiveFloat
from app.schemas.categoria.schemas  import Categoria
from app.schemas.centro_treinamento.schemas import CentroTreinamentoAtleta
from app.models.atleta.models import AtletaModel

from app.contrib.schemas import BaseSquema, OutMixin
class Atleta(BaseSquema):
    nome: Annotated[str, Field(description='Nome do atleta', example='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', example=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', example=75.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', example=1.70)]
    sexo: Annotated[str, Field(description='Sexo do atleta', example='M', max_length=1)]
    categoria: Annotated[Categoria, Field(description='Categoria do atleta')]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description='Centro de treinamento do atleta')]


class AtletaIn(Atleta):
    pass


class AtletaOut(Atleta, OutMixin):
    @classmethod
    def model_validate(cls, atleta: AtletaModel) -> "AtletaOut":

        categoria_dict = {
            "nome": atleta.categoria.nome,
        }
        centro_treinamento_dict = {
            "nome": atleta.centro_treinamento.nome,
        }

        return cls(
            id=str(atleta.id),
            nome=atleta.nome,
            cpf=atleta.cpf,
            idade=atleta.idade,
            peso=atleta.peso,
            altura=atleta.altura,
            sexo=atleta.sexo,
            created_at=atleta.created_at,
            categoria=Categoria(**categoria_dict),
            centro_treinamento=CentroTreinamentoAtleta(**centro_treinamento_dict),
        )

class AtletaUpdate(BaseSquema):
    nome: Annotated[Optional[str], Field(None, description='Nome do atleta', example='Joao', max_length=50)]
    idade: Annotated[Optional[int], Field(None, description='Idade do atleta', example=25)]