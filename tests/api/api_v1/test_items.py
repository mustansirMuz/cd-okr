from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from tests.utils.item import create_random_item


def test_create_item(client: TestClient, db: Session) -> None:
    data = {"title": "Foo", "description": "Fighters", "owner_id": 1}
    response = client.post(
        f"{settings.API_STR}{settings.API_V1_STR}/items/",
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == data["title"]
    assert content["description"] == data["description"]
    assert "id" in content
    assert "owner_id" in content


def test_read_item(client: TestClient, db: Session) -> None:
    item = create_random_item(db)
    response = client.get(
        f"{settings.API_STR}{settings.API_V1_STR}/items/{item.id}",
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == item.title
    assert content["description"] == item.description
    assert content["id"] == item.id
    assert content["owner_id"] == item.owner_id
