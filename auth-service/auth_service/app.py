from auth_service.db import conn_str
from auth_service.dtos.user_login import UserLoginDto
from auth_service.dtos.user_signup import UserSignupDto
from auth_service.helpers import check_password, hash_password, sign_jwt
from auth_service.models.user_model import User
from fastapi import FastAPI, HTTPException
from fastapi_sqlalchemy import DBSessionMiddleware, db

app = FastAPI()

# middlewares
app.add_middleware(DBSessionMiddleware, db_url=conn_str)


@app.post("/login", tags=["Auth"])
async def login(user: UserLoginDto):
    found_user = db.session.query(User).filter_by(email=user.email).first()

    if found_user is None:
        return HTTPException(status_code=404, detail="User not found")

    if check_password(user.password, found_user.password):
        return sign_jwt(str(found_user.id))


@app.post("/signup", tags=["Auth"])
async def signup(user: UserSignupDto):
    user_with_email = db.session.query(User).filter_by(email=user.email).first()

    if user_with_email is not None:
        return HTTPException(
            status_code=400, detail="User with this email already exists"
        )

    new_user = User(
        name=user.name, email=user.email, password=hash_password(user.password)
    )

    db.session.add(new_user)
    db.session.commit()

    return sign_jwt(str(new_user.id))
