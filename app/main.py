from fastapi import FastAPI
from datetime import datetime
from finance import quotes

feeder = quotes.Quotes()
app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "Hello World"}

@app.get("/ping")
async def pong():
    return {"pong": datetime.now().time()}

@app.get("/currency/{currency}")
async def get_currency(currency):
    return feeder.get(currency)
