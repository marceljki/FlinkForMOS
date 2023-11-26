import requests


def make_request(url, params, *args, print_response=False):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        # The request was successful
        data = response.json()
        if print_response:
            print(data)
        articles = data
        for arg in args:
            articles = articles.get(arg, [])

        for article in articles:
            print(article)
    else:
        # There was an error with the request
        print(f"Error: {response.status_code} - {response.text}")
