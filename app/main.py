import uvicorn
from fastapi import FastAPI
from app.api import users
from app.core.logging import setup_logging

app = FastAPI(title="User", version="1.0.1")
setup_logging()

app.include_router(users.router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
