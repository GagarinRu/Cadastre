import asyncio
import random
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.cadastre import Cadastre


class CRUDMCadastreAnswer(CRUDBase):
    async def get_answer_in(
        self,
        cadastre_id: int,
        session: AsyncSession,
    ) -> Optional[bool]:
        await asyncio.sleep(random.randint(1, 60))
        cadastre_answer = await session.execute(
            select(Cadastre.answer).where(
                Cadastre.id == cadastre_id
            )
        )
        cadastre_answer = cadastre_answer.scalars().first()
        return cadastre_answer


cadastre_crud = CRUDMCadastreAnswer(Cadastre)
