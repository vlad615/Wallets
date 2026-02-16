from os import getenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = getenv("DATABASE_URL")
    echo: bool = False


settings = Settings()
