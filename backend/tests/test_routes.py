import pytest
from unittest.mock import patch
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# ── Health ───────────────────────────────────────────────────────────


def test_health_returns_200(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_health_returns_ok_status(client):
    data = client.get("/health").get_json()
    assert data["status"] == "ok"


# ── POST /recipes ────────────────────────────────────────────────────


@patch("routes.recipes.generate_recipe")
@patch("routes.recipes.save_recipe")
def test_post_recipes_returns_200_with_valid_input(
    mock_save, mock_generate, client
):
    mock_generate.return_value = "mock recipe"
    mock_save.return_value = {"id": 1}

    response = client.post(
        "/recipes",
        json={"ingredients": "chicken, pasta"},
    )

    assert response.status_code == 200


@patch("routes.recipes.generate_recipe")
@patch("routes.recipes.save_recipe")
def test_post_recipes_returns_recipe_key(
    mock_save, mock_generate, client
):
    mock_generate.return_value = "mock recipe"
    mock_save.return_value = {"id": 1}

    data = client.post(
        "/recipes",
        json={"ingredients": "chicken"},
    ).get_json()

    assert "recipe" in data


def test_post_recipes_returns_400_with_empty_body(client):
    response = client.post("/recipes", json={})
    assert response.status_code == 400


def test_post_recipes_returns_400_with_missing_ingredients_key(client):
    response = client.post("/recipes", json={"food": "chicken"})
    assert response.status_code == 400


def test_post_recipes_returns_error_key_on_400(client):
    data = client.post("/recipes", json={}).get_json()
    assert "error" in data


@patch("routes.recipes.generate_recipe")
@patch("routes.recipes.save_recipe")
def test_post_recipes_calls_save_recipe(
    mock_save, mock_generate, client
):
    mock_generate.return_value = "mock recipe"
    mock_save.return_value = {"id": 1}

    client.post("/recipes", json={"ingredients": "eggs"})

    mock_save.assert_called_once()


# ── GET /recipes ─────────────────────────────────────────────────────


def test_get_recipes_returns_200(client):
    with patch("routes.recipes.get_all_recipes") as mock_get:
        mock_get.return_value = []
        response = client.get("/recipes")
        assert response.status_code == 200


def test_get_recipes_returns_recipes_key(client):
    with patch("routes.recipes.get_all_recipes") as mock_get:
        mock_get.return_value = []
        data = client.get("/recipes").get_json()
        assert "recipes" in data


def test_get_recipes_returns_a_list(client):
    with patch("routes.recipes.get_all_recipes") as mock_get:
        mock_get.return_value = [
            {"ingredients": "eggs", "recipe": "scrambled eggs"}
        ]
        data = client.get("/recipes").get_json()
        assert isinstance(data["recipes"], list)


# ── POST /substitutions ──────────────────────────────────────────────


@patch("routes.recipes.suggest_substitutions")
def test_substitutions_returns_200_with_valid_input(
    mock_suggest, client
):
    mock_suggest.return_value = ["oil", "margarine"]

    response = client.post(
        "/substitutions",
        json={"ingredient": "butter"},
    )

    assert response.status_code == 200


@patch("routes.recipes.suggest_substitutions")
def test_substitutions_returns_substitutions_key(
    mock_suggest, client
):
    mock_suggest.return_value = ["oil", "margarine"]

    data = client.post(
        "/substitutions",
        json={"ingredient": "butter"},
    ).get_json()

    assert "substitutions" in data


def test_substitutions_returns_400_with_empty_body(client):
    response = client.post("/substitutions", json={})
    assert response.status_code == 400


def test_substitutions_returns_error_key_on_400(client):
    data = client.post("/substitutions", json={}).get_json()
    assert "error" in data