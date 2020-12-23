from fastapi import FastAPI
from datetime import datetime
from entities.product import *

service = ProductService("etc/catalog.txt")

app = FastAPI()


@app.get("/ping")
async def pong():
    return {"pong": datetime.now().time()}


@app.get("/products")
async def ListProduct():
    p = service.products
    start = datetime.now()
    
    return {
        "time": datetime.now(),
        "elapsed-time": datetime.now() - start,
        "products": p
    }


@app.get("/currencies")
async def GetCurrencies():
    return {
        "currencies": service.currencies,
        "last-refresh": service.lastRefresh
    }


@app.get("/refresh_currencies")
async def RefreshCurrencies():
    start = datetime.now()
    service.refreshCurrencies()
    return {
        "time": datetime.now(),
        "elapsed-time": datetime.now() - start,
        "currencies": service.currencies,
        "last-refresh": service.lastRefresh
    }
