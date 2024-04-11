from uuid import uuid4

from pydantic import UUID4
from app.contrib.depends import DatabaseDependecy
from app.models.centro_treinamento.models import CentroTreinamentoModel
from app.schemas.centro_treinamento.schemas import CentroTreinamento, CentroTreinamentoOut
from sqlalchemy.future import select
from fastapi import APIRouter, Body, HTTPException, status

router = APIRouter()

@router.post('/',summary='Criar um novo Centro de Treinamento' ,status_code=status.HTTP_201_CREATED, response_model=CentroTreinamentoOut)

async def post(db_session: DatabaseDependecy, centro_treinamento_in:CentroTreinamento = Body(...)) -> CentroTreinamentoOut:
    centro_treinamento_out = CentroTreinamentoOut(id=uuid4(), **centro_treinamento_in.model_dump())
    centro_treinamemento_model = CentroTreinamentoModel(**centro_treinamento_out.model_dump())
    db_session.add(centro_treinamemento_model)
    await db_session.commit()

    return centro_treinamento_out

@router.get('/', summary='Trazer todas as categorias', status_code=status.HTTP_200_OK, response_model=list[CentroTreinamentoOut])
async def query(db_session: DatabaseDependecy) -> list[CentroTreinamentoOut]:
    centros_treinamentos_out: list[CentroTreinamentoOut] = (await db_session.execute(select(CentroTreinamentoModel))).scalars().all()
    return centros_treinamentos_out


@router.get('/{id}', summary='Consultar categoria pelo id', status_code=status.HTTP_200_OK, response_model=CentroTreinamentoOut)
async def query(id:UUID4, db_session: DatabaseDependecy) -> CentroTreinamentoOut:
    centro_treinamento_out: CentroTreinamentoOut = (await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id))).scalars().first()
    
    if not centro_treinamento_out:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Centro de Treinamento não encontrado: {id}') 
    return centro_treinamento_out