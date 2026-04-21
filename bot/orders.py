import os
import time
import hmac
import hashlib
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
SECRET = os.getenv("BINANCE_SECRET_KEY")

BASE_URL = "https://testnet.binancefuture.com"

def sign(params):
    query = urlencode(params)
    signature = hmac.new(
        SECRET.encode(),
        query.encode(),
        hashlib.sha256
    ).hexdigest()
    return f"{query}&signature={signature}"

headers = {
    "X-MBX-APIKEY": API_KEY
}

def place_market_order(symbol, side, quantity):
    params = {
        "symbol": symbol,
        "side": side,
        "type": "MARKET",
        "quantity": quantity,
        "timestamp": int(time.time() * 1000)
    }

    url = f"{BASE_URL}/fapi/v1/order"
    response = requests.post(url, headers=headers, data=sign(params))
    return response.json()


def place_limit_order(symbol, side, quantity, price):
    params = {
        "symbol": symbol,
        "side": side,
        "type": "LIMIT",
        "quantity": quantity,
        "price": price,
        "timeInForce": "GTC",
        "timestamp": int(time.time() * 1000)
    }

    url = f"{BASE_URL}/fapi/v1/order"
    response = requests.post(url, headers=headers, data=sign(params))
    return response.json()