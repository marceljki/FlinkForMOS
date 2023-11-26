from src.api.api_request import make_request
from src.api.config import Config

config = Config()
api_key = config.get("ALPHA_VANTAGE")

url = "https://www.alphavantage.co/query"
params = {
    "function": "NEWS_SENTIMENT",
    "ticker": "APPL",
    "date": "2023-11-26",
    "apikey": api_key,
}

make_request(url, params, "feed")

''' #Notes alpha vantage

'''
