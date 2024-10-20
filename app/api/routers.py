from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import check_cadastre_in, check_ping
from app.core.db import get_async_session
from app.crud.cadastre import cadastre_crud
from app.schemas.cadastre import CadastreBase

main_router = APIRouter()
SessionDep = Annotated[AsyncSession, Depends(get_async_session)]


@main_router.post(
    '/query',
    response_model=CadastreBase,
    tags=['Cadastre']
)
async def query(
    cadastre: CadastreBase,
    session: SessionDep
):
    """
    Ввод данных и сихранение их в базу данных.
    """
    new_cadastre = await cadastre_crud.create(
        cadastre,
        session
    )
    return new_cadastre


@main_router.get(
    '/ping',
    tags=['Ping']
)
async def ping():
    """
    Проверка доступности сервера.
    """
    ping = await check_ping()
    return ping


@main_router.get(
    '/result/{cadastre_id}',
    tags=['Result']
)
async def get_answer(
    cadastre_id: int,
    session: SessionDep,
):
    """
    Вывод данных из базу данных по id.
    """
    await check_cadastre_in(
        cadastre_id,
        session=session
    )
    new_answer = await cadastre_crud.get_answer_in(
        cadastre_id,
        session=session
    )
    return new_answer


@main_router.get(
    '/history',
    tags=['History']
)
async def get_all_cadastre(
    session: Annotated[AsyncSession, Depends(get_async_session)]
):
    """
    Получение из базы данных всей истории запросов.
    """
    history = await cadastre_crud.get_multi(session)
    return history
