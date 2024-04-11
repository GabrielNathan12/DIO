from uuid import uuid4

from pydantic import UUID4
from app.contrib.depends import DatabaseDependecy
from app.schemas.categoria.schemas import Categoria, CategoriaOut
from sqlalchemy.future import select
from fastapi import APIRouter, Body, HTTPException, status
from app.models.categoria.models import CategoriaModel
router = APIRouter()

@router.post('/',summary='Criar uma nova Categoria' ,status_code=status.HTTP_201_CREATED, response_model=CategoriaOut)

async def post(db_session: DatabaseDependecy, categoria_in:Categoria = Body(...)) -> CategoriaOut:
    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel(**categoria_out.model_dump())
    db_session.add(categoria_model)
    await db_session.commit()

    return categoria_out

@router.get('/', summary='Trazer todas as categorias', status_code=status.HTTP_200_OK, response_model=list[CategoriaOut])
async def query(db_session: DatabaseDependecy) -> list[CategoriaOut]:
    categorias: list[CategoriaOut] = (await db_session.execute(select(CategoriaModel))).scalars().all()
    return categorias


@router.get('/{id}', summary='Consultar um centro de treinamento pelo id', status_code=status.HTTP_200_OK, response_model=CategoriaOut)
async def query(id:UUID4, db_session: DatabaseDependecy) -> CategoriaOut:
    categoria: CategoriaOut = (await db_session.execute(select(CategoriaModel).filter_by(id=id))).scalars().first()
    
    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Categoria não encontrada: {id}') 
    return categoria