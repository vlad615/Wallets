from fastapi import APIRouter, Path

from shemas import Operation, Wallet

router = APIRouter(prefix="/api/v1/wallets")


# Получение баланса кошелька
@router.get("/{wallet_uuid}/")
async def get_balance(wallet_uuid: Wallet):
    balance = await balance(wallet_uuid)
    return balance


@router.post("/{wallet_uuid}/{operation}")
async def change_balance(wallet_uuid: Wallet, operation: Operation, amount: int):
    ...
