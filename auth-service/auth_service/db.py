import psycopg2
from auth_service.config import Config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

conn_str = f"postgresql+psycopg2://{Config.db_user}:{Config.db_password}@{Config.db_host}:{Config.db_port}/{Config.db_name}"

engine = create_engine(conn_str, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)


def init_db():
    # create if not exists
    conn = psycopg2.connect(
        dbname="postgres",  # connect to default to check
        user=Config.db_user,
        password=Config.db_password,
        host=Config.db_host,
        port=Config.db_port,
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(
        f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{Config.db_name}'"
    )
    db_exists = cur.fetchone()
    if not db_exists:
        cur.execute(f"CREATE DATABASE {Config.db_name}")
    cur.close()
    conn.close()

    # create all tables
    Base.metadata.create_all(bind=engine)
