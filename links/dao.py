from datetime import datetime

import logging

from links.models import Link, ClickLog
from settings.dao import BaseDAO

from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

logger = logging.getLogger(__name__)


class LinkDAO(BaseDAO):
    model = Link

    @classmethod
    async def delete_by_expire_at(cls, session: AsyncSession):
        query = delete(cls.model).where(cls.model.expires_at < datetime.now())
        try:
            result = await session.execute(query)
            await session.flush()
            return result.rowcount
        except SQLAlchemyError as e:
            await session.rollback()
            logger.error(f"Ошибка при удалении записей: {e}")
            raise e


class ClickLogDAO(BaseDAO):
    model = ClickLog
