from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Wallets(Base):
    __tablename__ = "wallets"
    uuid: Mapped[str] = mapped_column(primary_key=True)
    cash: Mapped[int]

# class Operations(Base):
#     id: int
#     date:
#     type:
#     wallet_uuid:
#     amount: int