from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from auth_service.config import Config

conn_str = f"postgresql://{Config.db_user}:{Config.db_password}@{Config.db_host}:{Config.db_port}/{Config.db_name}"

engine = create_engine(conn_str, echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)
