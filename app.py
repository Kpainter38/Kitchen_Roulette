import requests

API_KEY = ''


def get_recipes(ingredients):
    url = ''
    params = {
        'ingredients': ingredients,
        'number': 5,
        'apiKey': API_KEY
    }

    response = requests.get(url, params=params)