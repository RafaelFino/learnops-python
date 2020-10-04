from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/ping")
async def pong():
    return {"pong": datetime.now().time()}
