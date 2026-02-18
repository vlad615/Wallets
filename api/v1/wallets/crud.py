from database.wallet import Wallets
from uuid import UUID
from .shemas import Wallet, RequestOperation
from errors import OperationError
from sqlalchemy.ext.asyncio import AsyncSession


async def get_cash(session: AsyncSession, uuid: UUID) -> Wallets | None:
    return await session.get(Wallets, uuid)


async def new_wallet(session: AsyncSession, wallet: Wallet) -> Wallets:
    new_wallet = Wallets(**wallet.model_dump())
    session.add(new_wallet)
    await session.commit()
    await session.refresh(new_wallet)
    return new_wallet


async def make_operation(session: AsyncSession, operation: RequestOperation, uuid: UUID) -> Wallets | None:
    wallet = await get_cash(session, uuid)
    if not wallet:
        return None

    match operation.operation:
        case operation.operation.deposit:
            wallet.balance += operation.cash
        case _:
            if wallet.balance < operation.cash:
                raise OperationError("Недостаток средств", "На балансе меньше, чем вы планируете снять")
            else:
                wallet.balance -= operation.cash

    await session.commit()
    await session.refresh(wallet)
    return wallet

