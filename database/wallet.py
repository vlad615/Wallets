from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Wallets(Base):
    __tablename__ = "wallets"
    uuid: str
    cash: int

# class Operations(Base):
#     id: int
#     date:
#     type:
#     wallet_uuid:
#     amount: int