import os
from supabase import create_client, Client

_client: Client = None

def get_client() -> Client:
    global _client
    if _client is None:
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_KEY")
        _client = create_client(url, key)
    return _client

def save_recipe(ingredients: str, recipe: str) -> dict:
    client = get_client()
    response = (
        client.table("recipes")
        .insert({"ingredients": ingredients, "recipe": recipe})
        .execute()
    )
    return response.data[0] if response.data else {}

def get_all_recipes() -> list:
    client = get_client()
    response = (
        client.table("recipes")
        .select("id, ingredients, recipe, created_at")
        .order("created_at", desc=True)
        .execute()
    )
    return response.data if response.data else []