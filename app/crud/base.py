import asyncio
import random
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDBase:

    def __init__(self, model):
        self.model = model

    async def get(
        self,
        obj_id: int,
        session: AsyncSession,
    ):
        db_obj = await session.execute(
            select(self.model).where(
                self.model.id == obj_id
            )
        )
        return db_obj.scalars().first()

    async def get_multi(
        self,
        session: AsyncSession
    ):
        db_objs = await session.execute(select(self.model))
        return db_objs.scalars().all()

    async def create(
        self,
        obj_in,
        session: AsyncSession,
    ):
        obj_in_data = obj_in.dict()
        obj_in_data['created_at'] = datetime.today()
        obj_in_data['answer'] = random.choice((True, False))
        db_obj = self.model(**obj_in_data)
        await asyncio.sleep(random.randint(1, 60))
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj
