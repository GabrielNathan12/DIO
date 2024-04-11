from fastapi import APIRouter, status
from app.config.settings import client, database

router = APIRouter()

async def get_atletas():
    coolection = database['atletas']
    cursor = coolection.find({},{'_id':0})
    return await cursor.to_list(length=None)

@router.get('/',summary='Listar atletas', status_code=status.HTTP_200_OK)
async def get():
    data = await get_atletas()
    return data
