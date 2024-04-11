from pydantic import Field
from app.contrib.schemas import BaseSchema

class Categoria(BaseSchema):
     nome: str = Field(..., max_length=10, description='Nome da Categoria', example='natação')