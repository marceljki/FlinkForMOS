from src.api.api_request import make_request, filter_docs, to_json
from src.api.config import Config

config = Config()
NAME = "NY_TIMES"
news_api_key = config.get("%s" % NAME)


url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
params = {
    "q": "tesla",
    "begin_date": "20231126",
    "api-key": news_api_key,
}

docs = make_request(url, params, "response", "docs")
selected_keys = ["abstract", "snippet", "lead_paragraph", "web_url"]
filtered_docs = filter_docs(docs, selected_keys)
to_json(NAME, filtered_docs, config)

''' #Notes on ny times
We should get the data once a day at 2 AM on NY, which is 8 AM local time
Then we get all the news from the previous day

For evaluation of the article we can use the following attributes:
    - abstract
    - snippet
    - lead_paragraph
    - web-url (?)
'''
