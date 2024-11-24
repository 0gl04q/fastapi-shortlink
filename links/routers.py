import os

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import RedirectResponse
from pydantic import HttpUrl
from sqlalchemy.ext.asyncio import AsyncSession
from links.schemas import LinkModel
from links.dao import LinkDAO
from settings.session_maker import TransactionSessionDep, SessionDep
from utils.generators import generate_slug, generate_url

router = APIRouter(prefix='', tags=['links'])


@router.post('/generate')
async def generate(url: HttpUrl, session: AsyncSession = TransactionSessionDep) -> HttpUrl:
    link = await LinkDAO.find_one_or_none(session=session, filters=LinkModel(original_url=str(url)))
    if link:
        return link.short_url

    slug = generate_slug()
    while await LinkDAO.find_one_or_none(session=session, filters=LinkModel(slug=slug)):
        slug = generate_slug()

    short_url = generate_url(slug)
    await LinkDAO.add(session=session, values=LinkModel(original_url=str(url), short_url=str(short_url), slug=slug))
    return short_url


@router.get('/{slug}')
async def redirect_url(slug: str, session: AsyncSession = SessionDep):
    url_obj = await LinkDAO.find_one_or_none(session=session, filters=LinkModel(slug=slug))
    if not url_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return RedirectResponse(url_obj.original_url)


@router.get('/get_data/data')
def get_data():
    return ''.join(str(item) for item in os.listdir("/data"))
