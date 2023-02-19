from fastapi import FastAPI
from auth_service.models.user_model import User
from auth_service.dtos.user_login import UserLoginDto

app = FastAPI()


@app.post("/login", tags=["Auth"])
async def login(user: UserLoginDto):
    return {"data": user}


@app.post("/signup", tags=["Auth"])
async def signup():
    return {"data": "Hello World!"}
