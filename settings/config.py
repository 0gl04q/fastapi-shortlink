import os
from string import ascii_lowercase, ascii_uppercase, digits

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BASE_DIR: str = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    BASE_URL: str = '127.0.0.1:8000'
    HTTP_SCHEME: str = 'http'
    DATABASE_URL: str = f'sqlite+aiosqlite:///{BASE_DIR}/data/db.sqlite3'
    GENERATE_LIST: list = list(ascii_lowercase + ascii_uppercase + digits)
    REDIS_URL: str = 'redis://localhost:6379'
    model_config = SettingsConfigDict(env_file=f"{BASE_DIR}/.env")


settings = Settings()
database_url = settings.DATABASE_URL
