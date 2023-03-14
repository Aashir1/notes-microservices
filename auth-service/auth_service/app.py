from fastapi import FastAPI
from auth_service.models.user_model import User
from auth_service.dtos.user_login import UserLoginDto
from auth_service.dtos.user_signup import UserSignupDto
from fastapi_sqlalchemy import DBSessionMiddleware, db
from auth_service.db import conn_str

app = FastAPI()

# middlewares
app.add_middleware(DBSessionMiddleware, db_url=conn_str)


@app.post("/login", tags=["Auth"])
async def login(user: UserLoginDto):
    return {"data": user}


@app.post("/signup", tags=["Auth"])
async def signup(user: UserSignupDto):
    return {"data": user}
