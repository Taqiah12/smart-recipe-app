from flask import Blueprint, request, jsonify
from services.db_service import save_recipe, get_all_recipes
from services.ai_service import generate_recipe, suggest_substitutions

recipes_bp = Blueprint("recipes", __name__)


@recipes_bp.route("/recipes", methods=["POST"])
def create_recipe():
    data = request.get_json()

    if not data or not data.get("ingredients"):
        return jsonify({"error": "ingredients field is required"}), 400

    ingredients = data["ingredients"]

    try:
        recipe_text = generate_recipe(ingredients)
        save_recipe(ingredients, recipe_text)
        return jsonify({"recipe": recipe_text}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "failed to generate recipe", "details": str(e)}), 500


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

    try:
        result = suggest_substitutions(ingredient)
        return jsonify({"substitutions": result}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "failed to generate substitutions", "details": str(e)}), 500