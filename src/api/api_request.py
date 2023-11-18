import requests


def make_request(url, params):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        # The request was successful
        data = response.json()
        articles = data.get("articles", [])

        for article in articles:
            print(article["title"])
    else:
        # There was an error with the request
        print(f"Error: {response.status_code} - {response.text}")
