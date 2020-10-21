import requests
from datetime import datetime


class Product:
    id = ""
    name = ""
    prices = []

    def __init__(self, id, name, currency, price):
        self.id = id
        self.name = name
        self.prices = {currency: price}


class ProductService:
    products = []
    _urls = {"USD": "https://economia.awesomeapi.com.br/all/USD-BRL",
             "EUR": "https://economia.awesomeapi.com.br/all/EUR-BRL"}
    currencies = {}
    lastRefresh = ""

    def __init__(self, filePath):
        self._loadFromFile(filePath)
        self.refreshCurrencies()

    def _loadFromFile(self, path):
        ret = []

        f = open(path, "r")
        f.readline()

        for line in f:
            items = line.replace("\n", "").split("\t")
            ret.append(Product(items[0], items[1], "BRL", float(items[2])))

        f.close()

        self.products = ret

    def refreshCurrencies(self):
        ret = {"BRL": 1}
        for key in self._urls:
            r = requests.get(self._urls[key])
            ret[key] = r.json()[key]["ask"]

        self.currencies = ret

        for p in self.products:
            for currency in self.currencies:
                p.prices[currency] = round(float(p.prices["BRL"]) /
                                           float(self.currencies[currency]), 2)

        self.lastRefresh = datetime.now()
