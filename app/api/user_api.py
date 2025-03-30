from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.responses import JSONResponse
from core.db import get_session
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from services.user_service import UserService
from models.users import User
from schemas.user_schema import UserCreate,UserRead

router = APIRouter()
user_service = UserService()

@router.post(
    "/signup",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED
)
async def create_user_account(
    user_data : UserCreate , 
    session : AsyncSession = Depends(get_session)
):
    user_exists = await user_service.user_exists(user_data.email,session)
    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User with email already exists"
        )
    new_user = await user_service.create_user(user_data,session)

    return new_user    

