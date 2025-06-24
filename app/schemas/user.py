# app/schemas/user.py
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    full_name: str

class UserRead(BaseModel):
    id: int
    email: EmailStr
    full_name: str

    class Config:
        from_attributes = True
