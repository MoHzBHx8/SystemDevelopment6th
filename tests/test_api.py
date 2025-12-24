from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_expense():
    response = client.post(
        "/expenses/",
        json={
            "description": "Software Subscription",
            "amount": 20.0,
            "category": "Work",
        },
    )
    assert response.status_code == 200
    assert response.json()["description"] == "Software Subscription"


def test_create_invalid_expense():
    # Testing that the GT (Greater Than) 0 validation works
    response = client.post(
        "/expenses/",
        json={"description": "Refund", "amount": -10.0, "category": "Work"},
    )
    assert response.status_code == 422  # Unprocessable Entity
