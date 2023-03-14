from sqlalchemy import Column, String, UUID
from uuid import uuid4
from auth_service.db import Base
from pydantic import BaseModel


class User(Base):
    __tablename__ = "user"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    email = Column(String(80), unique=True)
    name = Column(String(255))
    password = Column(String(500))
