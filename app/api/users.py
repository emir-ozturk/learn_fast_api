# app/api/users.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate, UserRead
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository
from app.db import get_async_session  # DB bağlantı bağımlılığı

router = APIRouter(prefix="/users", tags=["users"])

async def get_user_service(db: AsyncSession = Depends(get_async_session)) -> UserService:
    repo = UserRepository(db)
    return UserService(repo)

@router.post("/", response_model=UserRead, status_code=201)
async def create_user(
    user_in: UserCreate,
    service: UserService = Depends(get_user_service)
):
    try:
        return await service.create_user(user_in)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[UserRead])
async def list_users(service: UserService = Depends(get_user_service)):
    return await service.list_users()

@router.get("/{user_id}", response_model=UserRead)
async def get_user(
    user_id: int,
    service: UserService = Depends(get_user_service)
):
    try:
        return await service.get_user(user_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="User not found")
