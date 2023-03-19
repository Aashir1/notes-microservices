import uvicorn
from auth_service.config import Config
from auth_service.db import init_db


def main():
    init_db()
    uvicorn.run(Config.app, host=Config.host, port=Config.port, reload=Config.debug)
