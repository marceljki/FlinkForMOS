from src.api.api_request import make_request, filter_docs, to_json
from src.api.config import Config
config = Config()
NAME = "NEWSAPI"
news_api_key = config.get("%s" % NAME)


url = "https://newsapi.org/v2/top-headlines"
params = {
    "q": "meta",
    "from": "2023-11-18",
    "sortBy": "publishedAt",
    "apiKey": news_api_key,
}

docs = make_request(url, params, "articles")
selected_keys = ["title", "description", "content", "url", "publishedAt"]
filtered_docs = filter_docs(docs, selected_keys)
to_json(NAME, filtered_docs, config)