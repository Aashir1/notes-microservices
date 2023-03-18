from fastapi import FastAPI, HTTPException
from auth_service.models.user_model import User
from auth_service.dtos.user_login import UserLoginDto
from auth_service.dtos.user_signup import UserSignupDto
from auth_service.helpers import check_password, sign_jwt
from fastapi_sqlalchemy import DBSessionMiddleware, db
from auth_service.db import conn_str, SessionLocal, Base, engine

app = FastAPI()

# middlewares
app.add_middleware(DBSessionMiddleware, db_url=conn_str)


@app.post("/login", tags=["Auth"])
async def login(user: UserLoginDto):
    found_user = db.session.query(User).filter_by(email=user.email).first()

    if found_user is None:
        return HTTPException(status_code=404, detail="User not found")

    if check_password(user.password, found_user.password):
        return sign_jwt(found_user.id)


@app.post("/signup", tags=["Auth"])
async def signup(user: UserSignupDto):
    return {"data": user}
