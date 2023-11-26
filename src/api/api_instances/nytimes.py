from src.api.api_request import make_request
from src.api.config import Config

config = Config()
news_api_key = config.get("NY_TIMES_KEY")


url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
params = {
    "q": "election",
    "begin_date": "20231126",
    "api-key": news_api_key,
}

make_request(url, params, "response", "docs")

''' #Notes on ny times
We should get the data once a day at 2 AM on NY, which is 8 AM local time
Then we get all the news from the previous day

For evaluation of the article we can use the following attributes:
    - abstract
    - snippet
    - lead_paragraph
    - web-url (?)
'''
