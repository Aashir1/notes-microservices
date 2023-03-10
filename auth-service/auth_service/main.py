import uvicorn
from auth_service.config import Config


def main():
    uvicorn.run(Config.app, port=Config.port, reload=Config.debug)
