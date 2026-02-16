from fastapi import APIRouter, Path
from uuid import UUID

from .shemas import Operation

router = APIRouter(prefix="/api/v1/wallets")


# Получение баланса кошелька
@router.get("/{wallet_uuid}/")
async def get_balance(wallet_uuid: UUID = Path(...)):
    pass


# Операции с балансом кошелька
@router.post("/{wallet_uuid}/{operation}")
async def change_balance(operation: Operation, amount: int, wallet_uuid: UUID = Path(...)):
    pass
