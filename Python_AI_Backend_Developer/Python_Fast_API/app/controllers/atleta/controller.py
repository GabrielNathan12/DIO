from pydantic import UUID4
from app.contrib.depends import DatabaseDependecy
from app.schemas.atleta.schemas import Atleta, AtletaOut, AtletaUpdate
from app.models.atleta.models import AtletaModel
from app.models.categoria.models import CategoriaModel
from app.models.centro_treinamento.models import CentroTreinamentoModel

from datetime import datetime
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status

router = APIRouter()

@router.post('/',summary='Criar novo Atleta' ,status_code=status.HTTP_201_CREATED, response_model=AtletaOut)

async def post(db_session: DatabaseDependecy, atleta_in:Atleta = Body(...)):
    
    categoria_nome = atleta_in.categoria.nome
    centro_treinamento_nome = atleta_in.centro_treinamento.nome

    categoria = (await db_session.execute(select(CategoriaModel).filter_by(nome=categoria_nome))).scalars().first()

    if not categoria:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'A categoria não foi encontrado: {categoria_nome}') 
    
    centro_treinamento = (await db_session.execute(select(CentroTreinamentoModel).filter_by(nome=centro_treinamento_nome))).scalars().first()

    if not centro_treinamento:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'O centro de treinamento não foi encontrado: {centro_treinamento_nome}') 

    try:
        atleta_out = AtletaOut(id=uuid4(),created_at=datetime.now() , **atleta_in.model_dump())
        atleta_model = AtletaModel(**atleta_out.model_dump(exclude={'categoria', 'centro_treinamento'}))
        atleta_model.categoria_id = categoria.pk_id
        atleta_model.centro_treinamento_id = centro_treinamento.pk_id
        db_session.add(atleta_model)
        await db_session.commit()
    except IntegrityError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'CPF já cadastrado')
    except Exception as e:
        error_message = str(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'Ocorreu ao inserir os dados no Banco: {error_message}') 

    
    return atleta_out

@router.get('/', summary='Consultar todos os Atletas', status_code=status.HTTP_200_OK, response_model=list[AtletaOut])
async def get(db_session: DatabaseDependecy) -> list[AtletaOut]:
    atletas: list[AtletaModel] = (await db_session.execute(select(AtletaModel))).scalars().all()
    
    return [AtletaOut.model_validate(atleta) for atleta in atletas]


@router.get('/{id}', summary='Um Atleta', status_code=status.HTTP_200_OK, response_model=AtletaOut)
async def get_id(id:UUID4, db_session: DatabaseDependecy) -> AtletaOut:
   atleta: AtletaOut = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()

   if not atleta:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Atleta não encontrado: {id}')
   
   return atleta


@router.patch('/{id}', summary='Editar um atleta', status_code=status.HTTP_200_OK, response_model=AtletaOut)
async def patch(id:UUID4, db_session: DatabaseDependecy, atleta_in: AtletaUpdate = Body(...)) -> AtletaOut:
    atleta: AtletaOut = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()

    if not atleta:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Atleta não encontrado: {id}')
    
    atleta_update = atleta_in.model_dump(exclude_unset=True)

    for key, value in atleta_update.items():
       setattr(atleta, key, value)
    
    await db_session.commit()
    await db_session.refresh(atleta)

    return atleta

@router.delete('/{id}', summary='Deletar Atleta', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id:UUID4, db_session: DatabaseDependecy) -> None:
    atleta: AtletaOut = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()

    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Atleta não encontrado: {id}')
    
    await db_session.delete(atleta)
    await db_session.commit()