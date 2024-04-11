import datetime
from pydantic import UUID4, BaseModel, Field

class BaseSchema(BaseModel):
    class Config:
        extra = 'forbid'
        from_attributes = True

class OutMinix(BaseSchema):
    id: UUID4 = Field(..., description='Identificador')
    created_at: datetime = Field(..., description='Data de criação')