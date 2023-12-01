import requests
import json


def make_request(url, params, *args, print_response=False):
    response = requests.get(url, params=params)

    res = []
    if response.status_code == 200:
        # The request was successful
        data = response.json()
        if print_response:
            print(data)
        articles = data
        for arg in args:
            articles = articles.get(arg, [])

        for article in articles:
            res.append(article)
    else:
        # There was an error with the request
        print(f"Error: {response.status_code} - {response.text}")

    return res


def filter_docs(docs: dict, selected_keys: []) -> list:
    res = []
    for doc in docs:
        try:
            filered_doc = {key: doc[key] for key in selected_keys}
            res.append(filered_doc)
        except KeyError:
            print("ERROR: Could not find key Keys: %s\n" % selected_keys)

    return res


def to_json(filename, docs, config):
    filepath = config.get_out_path() + filename + ".json"
    with open(filepath, "w") as outfile:
        json.dump(docs, outfile)
