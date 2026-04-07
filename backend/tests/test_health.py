from app import create_app


def test_health_returns_ok():
    app = create_app()
    client = app.test_client()

    response = client.get("/health")
    data = response.get_json()

    assert response.status_code == 200
    assert data == {"status": "ok"}