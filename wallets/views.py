from fastapi import APIRouter, Path
from uuid import UUID, uuid4

from .shemas import RequestOperation

router = APIRouter(prefix="/api/v1/wallets")


# Получение баланса кошелька
@router.get("/{wallet_uuid}/")
async def get_balance(wallet_uuid: UUID = Path(...)):
    pass


# Операции с балансом кошелька
@router.post("/{wallet_uuid}/{operation}/")
async def change_balance(operation: RequestOperation, wallet_uuid: UUID = Path(...)):
    pass


@router.post("/new_wallet/")
async def create_wallet():
    new_id = uuid4()
    return {"wallet_uuid": new_id}
