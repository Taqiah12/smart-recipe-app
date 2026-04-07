from app import create_app


def test_create_recipe_success(monkeypatch):
    app = create_app()
    client = app.test_client()

    def mock_generate_recipe(ingredients):
        return "Mock recipe output"

    def mock_save_recipe(ingredients, recipe):
        return {"id": 1, "ingredients": ingredients, "recipe": recipe}

    monkeypatch.setattr("routes.recipes.generate_recipe", mock_generate_recipe)
    monkeypatch.setattr("routes.recipes.save_recipe", mock_save_recipe)

    response = client.post("/recipes", json={"ingredients": "chicken, rice"})
    data = response.get_json()

    assert response.status_code == 200
    assert "recipe" in data
    assert data["recipe"] == "Mock recipe output"


def test_create_recipe_missing_body():
    app = create_app()
    client = app.test_client()

    response = client.post("/recipes", json={})
    data = response.get_json()

    assert response.status_code == 400
    assert data["error"] == "ingredients field is required"


def test_create_recipe_missing_ingredients_key():
    app = create_app()
    client = app.test_client()

    response = client.post("/recipes", json={"name": "test"})
    data = response.get_json()

    assert response.status_code == 400
    assert data["error"] == "ingredients field is required"


def test_create_recipe_value_error(monkeypatch):
    app = create_app()
    client = app.test_client()

    def mock_generate_recipe(ingredients):
        raise ValueError("ingredients are required")

    monkeypatch.setattr("routes.recipes.generate_recipe", mock_generate_recipe)

    response = client.post("/recipes", json={"ingredients": "   "})
    data = response.get_json()

    assert response.status_code == 400
    assert data["error"] == "ingredients are required"


def test_create_recipe_unexpected_error(monkeypatch):
    app = create_app()
    client = app.test_client()

    def mock_generate_recipe(ingredients):
        raise Exception("Gemini API failed")

    monkeypatch.setattr("routes.recipes.generate_recipe", mock_generate_recipe)

    response = client.post("/recipes", json={"ingredients": "chicken"})
    data = response.get_json()

    assert response.status_code == 500
    assert data["error"] == "failed to generate recipe"
    assert "details" in data


def test_list_recipes_success(monkeypatch):
    app = create_app()
    client = app.test_client()

    mock_recipes = [
        {
            "id": 1,
            "ingredients": "chicken, rice",
            "recipe": "Recipe 1",
            "created_at": "2026-04-04T12:00:00",
        },
        {
            "id": 2,
            "ingredients": "egg, bread",
            "recipe": "Recipe 2",
            "created_at": "2026-04-04T13:00:00",
        },
    ]

    def mock_get_all_recipes():
        return mock_recipes

    monkeypatch.setattr("routes.recipes.get_all_recipes", mock_get_all_recipes)

    response = client.get("/recipes")
    data = response.get_json()

    assert response.status_code == 200
    assert "recipes" in data
    assert len(data["recipes"]) == 2


def test_list_recipes_empty(monkeypatch):
    app = create_app()
    client = app.test_client()

    def mock_get_all_recipes():
        return []

    monkeypatch.setattr("routes.recipes.get_all_recipes", mock_get_all_recipes)

    response = client.get("/recipes")
    data = response.get_json()

    assert response.status_code == 200
    assert data["recipes"] == []


def test_substitutions_success(monkeypatch):
    app = create_app()
    client = app.test_client()

    def mock_suggest_substitutions(ingredient):
        return "Use olive oil, margarine, or yogurt"

    monkeypatch.setattr(
        "routes.recipes.suggest_substitutions", mock_suggest_substitutions
    )

    response = client.post("/substitutions", json={"ingredient": "butter"})
    data = response.get_json()

    assert response.status_code == 200
    assert "substitutions" in data
    assert "olive oil" in data["substitutions"]


def test_substitutions_missing_body():
    app = create_app()
    client = app.test_client()

    response = client.post("/substitutions", json={})
    data = response.get_json()

    assert response.status_code == 400
    assert data["error"] == "ingredient field is required"


def test_substitutions_missing_ingredient_key():
    app = create_app()
    client = app.test_client()

    response = client.post("/substitutions", json={"ingredients": "butter"})
    data = response.get_json()

    assert response.status_code == 400
    assert data["error"] == "ingredient field is required"


def test_substitutions_value_error(monkeypatch):
    app = create_app()
    client = app.test_client()

    def mock_suggest_substitutions(ingredient):
        raise ValueError("ingredient is required")

    monkeypatch.setattr(
        "routes.recipes.suggest_substitutions", mock_suggest_substitutions
    )

    response = client.post("/substitutions", json={"ingredient": "   "})
    data = response.get_json()

    assert response.status_code == 400
    assert data["error"] == "ingredient is required"


def test_substitutions_unexpected_error(monkeypatch):
    app = create_app()
    client = app.test_client()

    def mock_suggest_substitutions(ingredient):
        raise Exception("Gemini substitution failed")

    monkeypatch.setattr(
        "routes.recipes.suggest_substitutions", mock_suggest_substitutions
    )

    response = client.post("/substitutions", json={"ingredient": "milk"})
    data = response.get_json()

    assert response.status_code == 500
    assert data["error"] == "failed to generate substitutions"
    assert "details" in data
