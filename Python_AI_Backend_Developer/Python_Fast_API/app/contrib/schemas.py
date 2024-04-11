from typing import Annotated
from pydantic import BaseModel, Field
from pydantic import UUID4
from datetime import datetime
class BaseSquema(BaseModel):
    class Config:
        extra = 'forbid'
        from_attrbutes = True

class OutMixin(BaseSquema):
    id: Annotated[UUID4, Field(description='Identificador')]
    created_at: Annotated[datetime, Field(description='Data criação')]