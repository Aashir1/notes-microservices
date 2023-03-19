from pydantic import BaseModel, EmailStr


class UserSignupDto(BaseModel):
    email: EmailStr
    password: str
    name: str
