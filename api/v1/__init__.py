from fastapi import APIRouter
from .wallets.views import router as wallets_router

router = APIRouter(prefix="/v1")

router.include_router(wallets_router)