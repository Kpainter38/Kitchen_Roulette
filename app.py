import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ.get("API_KEY")


def get_recipes(ingredients):
    url = 'https://api.spoonacular.com/recipes/findByIngredients'
    params = {
        'ingredients': ingredients,
        'number': 5,
        'apiKey': API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None


if __name__ == '__main__':
    ingredients = input("Enter ingredients separated by commas: ")
    recipes = get_recipes(ingredients)

    if recipes:
        for idx, recipe in enumerate(recipes):
            print(f"{idx + 1}. {recipe['title']}")
            print(f" - Used ingredients: {', '.join([ingredient['name'] for ingredient in recipe['usedIngredients']])}")
            print(
                f" - Missing ingredients: {', '.join([ingredient['name'] for ingredient in recipe['missedIngredients']])}")
            print(f" - Recipe link: https://spoonacular.com/recipes/{recipe['title'].replace(' ', '-')}-{recipe['id']}")
            print(f" - Image: {recipe['image']}")
            print()
    else:
        print("No recipes found.")
