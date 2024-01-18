import requests
import wikipedia


def wikipedia_search(query):
    results = wikipedia.summary(query, sentences=2)
    return results

def jokes():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]
