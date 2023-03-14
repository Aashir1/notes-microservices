import uvicorn
from auth_service.config import Config


def main():
    uvicorn.run(Config.app, host=Config.host, port=Config.port, reload=Config.debug)
