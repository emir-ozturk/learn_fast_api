import uvicorn
from fastapi import FastAPI
from app.api import users
from app.core.logging import setup_logging

app = FastAPI(title="User", version="1.0.1")
setup_logging()

app.include_router(users.router)

@app.on_event("startup")
async def startup_event():
    """Create database tables on startup"""
    from sqlalchemy.ext.asyncio import create_async_engine
    from app.models.user import Base
    from app.core.config import settings
    
    engine = create_async_engine(settings.database_url)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
