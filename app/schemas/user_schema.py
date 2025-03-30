from pydantic import BaseModel, ConfigDict, EmailStr, Field
from datetime import date, datetime


class UserBase(BaseModel):
    email : EmailStr
    name : str | None = Field(default=None,max_length=30)
    username : str = Field(max_length=20)
    
   
    
class UserCreate(UserBase):
    password : str = Field(min_length=6)


class UserRead(UserBase):
    id : int
   

