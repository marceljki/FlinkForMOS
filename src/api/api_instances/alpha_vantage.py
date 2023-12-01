from src.api.api_request import make_request, filter_docs, to_json
from src.api.config import Config

NAME = "ALPHA_VANTAGE"
config = Config()
api_key = config.get(NAME)
out_path = config.get_out_path()

url = "https://www.alphavantage.co/query"
params = {
    "function": "NEWS_SENTIMENT",
    "ticker": "APPL",
    "date": "2023-11-26",
    "apikey": api_key,
}

docs = make_request(url, params, "feed")
selected_keys = ["title", "summary", "overall_sentiment_score", "time_published", "url"]
filtered_docs = filter_docs(docs, selected_keys)
to_json(NAME, filtered_docs, config)
''' #Notes alpha vantage

'''
