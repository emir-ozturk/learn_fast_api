# app/services/user_service.py
from typing import List
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserRead

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def get_user(self, user_id: int) -> UserRead:
        user = await self.repo.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return UserRead.model_validate(user)

    async def list_users(self) -> List[UserRead]:
        users = await self.repo.list()
        return [UserRead.model_validate(u) for u in users]

    async def create_user(self, user_in: UserCreate) -> UserRead:
        user = await self.repo.create(user_in)
        return UserRead.model_validate(user)
