from pydantic import BaseModel
from enum import Enum
from uuid import UUID


class Operation(str, Enum):
    deposit = "deposit"
    withdrow = "withdrow"


class Wallet(BaseModel):
    wallet_id: UUID
    cash: int | None
