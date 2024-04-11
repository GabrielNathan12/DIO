from app.configs.database import get_sessiont
from fastapi import Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession


DatabaseDependecy = Annotated[AsyncSession, Depends(get_sessiont)]