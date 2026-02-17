from enum import Enum
from pydantic import BaseModel, Field


class Operation(str, Enum):
    deposit = "deposit"
    withdrow = "withdrow"


class RequestOperation(BaseModel):
    operation: Operation
    cash: int = Field(gt=0)

