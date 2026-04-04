from flask import Blueprint, request, jsonify
from services.db_service import save_recipe, get_all_recipes

# ↓ Uncomment this line once Moeez merges his ai_service branch
# from services.ai_service import generate_recipe, suggest_substitutions

recipes_bp = Blueprint("recipes", __name__)

@recipes_bp.route("/recipes", methods=["POST"])
def create_recipe():
    data = request.get_json()

    if not data or not data.get("ingredients"):
        return jsonify({"error": "ingredients field is required"}), 400

    ingredients = data["ingredients"]

    # ↓ Replace this line with: recipe_text = generate_recipe(ingredients)
    #   once Moeez's branch is merged
    recipe_text = f"Placeholder recipe for: {ingredients}"

    save_recipe(ingredients, recipe_text)

    return jsonify({"recipe": recipe_text}), 200

@recipes_bp.route("/recipes", methods=["GET"])
def list_recipes():
    recipes = get_all_recipes()
    return jsonify({"recipes": recipes}), 200

@recipes_bp.route("/substitutions", methods=["POST"])
def get_substitutions():
    data = request.get_json()

    if not data or not data.get("ingredient"):
        return jsonify({"error": "ingredient field is required"}), 400

    ingredient = data["ingredient"]

    # ↓ Replace this line with: result = suggest_substitutions(ingredient)
    #   once Moeez's branch is merged
    result = f"Placeholder substitution for: {ingredient}"

    return jsonify({"substitutions": result}), 200