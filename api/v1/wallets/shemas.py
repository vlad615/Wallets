from enum import Enum
from pydantic import BaseModel, Field, ConfigDict


class Operation(str, Enum):
    deposit = "deposit"
    withdrow = "withdrow"


class RequestOperation(BaseModel):
    operation: Operation
    cash: int = Field(gt=0)


class Wallet(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    balance: int = 0

