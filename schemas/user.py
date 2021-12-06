from pydantic import BaseModel
from typing import Optional


class UserDataModel(BaseModel):
    password: str
    avatar: Optional[str] = None


class UserDataResponseModel(BaseModel):
    avatar: Optional[str] = None


class UserRegistrationModel(BaseModel):
    username: str
    password: str
