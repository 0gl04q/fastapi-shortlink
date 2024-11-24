import logging

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from links.routers import router as links_router

logger = logging.getLogger(__name__)

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
app.include_router(links_router)
