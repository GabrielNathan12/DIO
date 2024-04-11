from app.contrib.schemas import BaseSquema
from typing import Annotated
from pydantic import Field
from pydantic import UUID4
class Categoria(BaseSquema):
    nome: Annotated[str, Field(description='Categoria', example='Natação', max_length=10)]

class CategoriaOut(Categoria):
    id: Annotated[UUID4, Field(description='Identificador')]