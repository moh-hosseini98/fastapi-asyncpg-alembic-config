from pydantic import EmailStr
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.users import User
from schemas.user_schema import UserCreate


class UserService:
    async def get_user_by_email(self,email : EmailStr,session:AsyncSession):
        stmt = select(User).where(User.email == email)
        result = await session.execute(stmt)
        return result.scalars().first()
    
    async def user_exists(self , email : EmailStr , session : AsyncSession):
        user = await self.get_user_by_email(email,session)
        return True if user is not None else False
    
    async def create_user(self,user_data : UserCreate , session : AsyncSession):
        user_data_dict = user_data.model_dump()
        new_user = User(**user_data_dict)
        session.add(new_user)
        await session.commit()
        return new_user