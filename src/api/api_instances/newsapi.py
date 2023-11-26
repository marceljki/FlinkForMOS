from src.api.api_request import make_request
from src.api.config import Config
config = Config()
news_api_key = config.get("NEWSAPI")


url = "https://newsapi.org/v2/top-headlines"
params = {
    "q": "meta",
    "from": "2023-11-18",
    "sortBy": "publishedAt",
    "apiKey": news_api_key,
}

make_request(url, params, "articles")
