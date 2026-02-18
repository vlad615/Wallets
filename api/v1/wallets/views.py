from fastapi import APIRouter, Path, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from starlette.exceptions import HTTPException

from database import db
from .crud import get_cash, new_wallet, make_operation
from .shemas import RequestOperation, Wallet

router = APIRouter(prefix="/wallets")


# Получение баланса кошелька
@router.get("/{wallet_uuid}/", response_model=Wallet)
async def get_balance(wallet_uuid: UUID = Path(...), session: AsyncSession = Depends(db.get_session)):
    result = await get_cash(session, wallet_uuid)
    if result:
        return result
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Wallet {wallet_uuid} not found")


# Операции с балансом кошелька
@router.post("/{wallet_uuid}/operation/", response_model=Wallet)
async def change_balance(operation: RequestOperation, wallet_uuid: UUID = Path(...),
                         session: AsyncSession = Depends(db.get_session)):
    result = await make_operation(session, operation, wallet_uuid)
    if result:
        return result
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Wallet {wallet_uuid} not found")


@router.post("/new_wallet/", response_model=Wallet)
async def create_wallet(balance: Wallet, session: AsyncSession = Depends(db.get_session)):
    return await new_wallet(session, balance)
