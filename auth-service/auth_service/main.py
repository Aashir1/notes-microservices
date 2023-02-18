from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"data": "Hello World!"}
