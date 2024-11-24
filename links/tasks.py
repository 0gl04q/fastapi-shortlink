from settings.session_maker import session_manager
from celery import shared_task
from links.dao import LinkDAO
import asyncio


async def async_delete_links():
    async with session_manager.create_session() as session:
        async with session_manager.transaction(session):
            await LinkDAO.delete_by_expire_at(session=session)


@shared_task
def delete_links():
    asyncio.run(async_delete_links())
