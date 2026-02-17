from uuid import uuid4

from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Wallets(Base):
    __tablename__ = "wallets"
    uuid: Mapped[str] = mapped_column(primary_key=True, default=uuid4())
    balance: Mapped[int] = mapped_column(nullable=False, default=0)

# class Operations(Base):
#     id: int
#     date:
#     type:
#     wallet_uuid:
#     amount: int