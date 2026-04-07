import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)


def generate_recipe(ingredients: str) -> str:
    if not ingredients or not ingredients.strip():
        raise ValueError("ingredients are required")

    if not GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY is not set")

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
    You are a helpful recipe assistant.
    The user has these ingredients: {ingredients}

    Generate:
    1. A recipe name
    2. Ingredients list
    3. Step-by-step instructions
    4. Short nutrition note

    Keep it practical and easy to cook at home.
    """

    response = model.generate_content(prompt)
    return response.text.strip()


def suggest_substitutions(ingredient: str) -> str:
    if not ingredient or not ingredient.strip():
        raise ValueError("ingredient is required")

    if not GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY is not set")

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
    You are a cooking assistant.
    Suggest 3 practical substitutions for this ingredient: {ingredient}

    For each substitute, explain briefly when it works best.
    """

    response = model.generate_content(prompt)
    return response.text.strip()
