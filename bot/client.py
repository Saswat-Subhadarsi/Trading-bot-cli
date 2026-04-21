# Placeholder for future Binance client abstraction.
# Current implementation uses direct REST API calls in orders.py.
# Due to so many problems in the python libraries i did not think
# it would be easy to use and it was easy using REST.
from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

class BinanceClient:
    def __init__(self):
        self.client = Client(
            os.getenv("BINANCE_API_KEY"),
            os.getenv("BINANCE_SECRET_KEY")
        )

        
        self.client.API_URL = "https://testnet.binancefuture.com/fapi"

    def place_order(self, **kwargs):
        return self.client.futures_create_order(**kwargs)