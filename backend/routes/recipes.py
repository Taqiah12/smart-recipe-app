from flask import Blueprint, request, jsonify

recipes_bp = Blueprint("recipes", __name__)

@recipes_bp.route("/recipes", methods=["POST"])
def create_recipe():
    return jsonify({"recipe": "coming soon"}), 200

@recipes_bp.route("/recipes", methods=["GET"])
def list_recipes():
    return jsonify({"recipes": []}), 200