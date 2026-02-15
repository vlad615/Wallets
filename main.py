from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class Operation(str, Enum):
    deposit = "deposit"
    withdrow = "withdrow"

# Получение баланса кошелька
@app.get("/api/v1/wallets/{wallet_uuid}/")
async def get_balance(wallet_uuid: str):
    balance = await balance(wallet_uuid)
    return balance


@app.post("/api/v1/wallets/{wallet_uuid}/{operation}")
async def change_balance(wallet_uuid: str, operation: Operation, amount: int):
    ...

