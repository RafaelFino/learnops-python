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
    return {
        "time": datetime.now(),
        "products": service.products
    }


@app.get("/currencies")
async def GetCurrencies():
    return {
        "currencies": service.currencies,
        "last-refresh": service.lastRefresh
    }


@app.get("/refresh_currencies")
async def RefreshCurrencies():
    service.refreshCurrencies()
    return {
        "currencies": service.currencies,
        "last-refresh": service.lastRefresh
    }
