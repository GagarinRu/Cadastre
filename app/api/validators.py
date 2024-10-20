from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Cadastre
from app.crud.cadastre import cadastre_crud


async def check_cadastre_in(
    cadastre_id: int,
    session: AsyncSession,
) -> Cadastre:
    cadastre = await cadastre_crud.get(
        obj_id=cadastre_id, session=session
    )
    if not cadastre:
        raise HTTPException(
            status_code=404,
            detail='Cadaster не найден!'
        )
    return cadastre


async def check_ping(
):
    ping = {'detail': 'Сервер доступен'}
    if not ping:
        raise HTTPException(
            status_code=500,
            detail='Внутренняя ошибка сервера',
        )
    return ping
