from sqlalchemy.orm import Session

from app import crud
from app.schemas.item import ItemCreate, ItemUpdate
from tests.utils import random_lower_string


def test_create_item(db: Session):
    title = random_lower_string()
    description = random_lower_string()
    owner_id = 1
    item_in = ItemCreate(title=title, description=description, owner_id=owner_id)
    item = crud.item.create(db=db, obj_in=item_in)
    assert item.title == title
    assert item.description == description
    crud.item.remove(db=db, id=item.id)


def test_get_item(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    owner_id = 1
    item_in = ItemCreate(title=title, description=description, owner_id=owner_id)
    item = crud.item.create(db=db, obj_in=item_in)
    stored_item = crud.item.get(db=db, id=item.id)
    assert stored_item
    assert item.id == stored_item.id
    assert item.title == stored_item.title
    assert item.description == stored_item.description
    assert item.owner_id == stored_item.owner_id
    crud.item.remove(db=db, id=item.id)


def test_update_item(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    owner_id = 1
    item_in = ItemCreate(title=title, description=description, owner_id=owner_id)
    item = crud.item.create(db=db, obj_in=item_in)
    description2 = random_lower_string()
    item_update = ItemUpdate(description=description2)
    item2 = crud.item.update(db=db, db_obj=item, obj_in=item_update)
    assert item.id == item2.id
    assert item.title == item2.title
    assert item2.description == description2
    assert item.owner_id == item2.owner_id
    crud.item.remove(db=db, id=item.id)


def test_delete_item(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    owner_id = 1
    item_in = ItemCreate(title=title, description=description, owner_id=owner_id)
    item = crud.item.create(db=db, obj_in=item_in)
    item2 = crud.item.remove(db=db, id=item.id)
    item3 = crud.item.get(db=db, id=item.id)
    assert item3 is None
    assert item2.id == item.id
    assert item2.title == title
    assert item2.description == description
