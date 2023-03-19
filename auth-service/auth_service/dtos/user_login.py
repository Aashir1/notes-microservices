from pydantic import BaseModel, EmailStr


class UserLoginDto(BaseModel):
    email: EmailStr
    password: str
