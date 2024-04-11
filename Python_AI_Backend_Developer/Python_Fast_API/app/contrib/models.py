from uuid import uuid4
from mongoengine import Document, UUIDField

class BaseModel(Document):
    id = UUIDField(primary_key=True, default=uuid4)