from enum import Enum
from uuid import UUID, uuid4
from pydantic import BaseModel, Field


class Operation(str, Enum):
    deposit = "deposit"
    withdrow = "withdrow"


class WalletsBase(BaseModel):
    cash: int


class Wallets(WalletsBase):
    uuid: UUID = Field(default_factory=uuid4)
