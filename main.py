from fastapi import FastAPI
import uvicorn

from wallets import wallets_router

app = FastAPI()
app.include_router(wallets_router)

if __name__ == "__main__":
    uvicorn.run(app, reload=True)
