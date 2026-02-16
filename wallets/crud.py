from database.wallet import Wallets
from sqlalchemy.engine import Result
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def get_cash(session: AsyncSession, uuid: str) -> Result:
    state = select(Wallets).where(Wallets.uuid == uuid)
    result: Result = await session.execute(state)
    return result
