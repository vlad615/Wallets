from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import uvicorn

from errors import OperationError
from database import Base, db

from api import router as api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db.engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
        yield

app = FastAPI(lifespan=lifespan)


@app.exception_handler(OperationError)
async def operation_error_handler(request: Request, exc: OperationError):
    return JSONResponse(status_code=409, content={"name": exc.name, "message": exc.massage})


app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, reload=True)
