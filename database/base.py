from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from .config import settings


class Base(DeclarativeBase):
    __abstract__ = True
    pass


class DatabaseEngine:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(url=url, echo=echo)
        self.session = async_sessionmaker(bind=self.engine, autoflush=False, expire_on_commit=False)


db = DatabaseEngine(settings.db_url, True)
