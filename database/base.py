from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_scoped_session, AsyncSession
from asyncio import current_task

from .config import settings


class Base(DeclarativeBase):
    __abstract__ = True
    pass


class DatabaseEngine:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(url=url, echo=echo)
        self.session_maker = async_sessionmaker(bind=self.engine, autoflush=False, expire_on_commit=False)

    def get_scope_session(self):
        session = async_scoped_session(session_factory=self.session_maker,
                                       scopefunc=current_task)
        return session

    async def get_session(self) -> AsyncSession:
        async with self.session_maker() as session:
            yield session
            await session.close()



db = DatabaseEngine(settings.db_url, settings.echo)
