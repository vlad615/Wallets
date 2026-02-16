from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn

from database import Base, db

from wallets import wallets_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db.engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)


app = FastAPI()
app.include_router(wallets_router)

if __name__ == "__main__":
    uvicorn.run(app, reload=True)
