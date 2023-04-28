from sqlalchemy.orm import Session
from database.models import Notes, ClientData
from schema.schemas import NotesSchema
import facebook
import requests


def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Notes).offset(skip).limit(limit).all()


def get_notes_by_id(db: Session, notes_id: int):
    return db.query(Notes).filter(Notes.id == notes_id).first()


def create_notes(db: Session, notes: NotesSchema):
    notes = Notes(
        title=notes.title,
        description=notes.description,
        check_in=notes.check_in,
        created_at=notes.created_at,
    )
    db.add(notes)
    db.commit()
    db.refresh(notes)
    return notes


def remove_notes(db: Session, notes_id: int):
    notes = get_notes_by_id(db=db, notes_id=notes_id)
    db.delete(notes)
    db.commit()


def update_notes(
    db: Session,
    notes_id: int,
    title: str,
    description: str,
    check_in: bool,
):
    notes = get_notes_by_id(db=db, notes_id=notes_id)
    notes.title = title
    notes.description = description
    notes.check_in = check_in
    db.commit()
    db.refresh(notes)
    return notes


def create_client(db: Session):

    url = "https://graph.facebook.com/v16.0/me?fields=name%2Cemail&access_token=EAASPaTEoZANoBAMbCeSPBzr9Hr0pdXdlO4IZCZCW2bZCtG7XZCgzET2MM1JlXs4ZAd1YeqzMeqzcPKgodm61eNh4lVlAsZAGKSFkyLWXx8CfLLhfZBVRuCh4cdsPc3nfZCfqKQswmPPUyahYQZAKfDA4IxqmqS44kaMM7ZCo4VhZCZCa4V0viY46dhJxpOl9EL3EuiugxAIcyrW1EUoUxjPip2ZBSDSDUDf1MKumEY5k2N4TVqEk8ZAe2xi8up1"
    response = requests.get(url)
    user = response.json()
    user = ClientData(
        # id=user["id"],
        name=user["name"],
        email=user["email"],
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ClientData).offset(skip).limit(limit).all()