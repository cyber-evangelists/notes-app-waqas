from sqlalchemy.orm import Session
from database.models import Notes, FacebookAuthUsers
from schema.schemas import NotesSchema, FacebookAuthUsersSchema
from sqlalchemy import BINARY
from datetime import datetime
from fastapi import UploadFile, File


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


def create_users(db: Session, users: FacebookAuthUsersSchema):
    users = FacebookAuthUsers(access_token=users.access_token)
    db.add(users)
    db.commit()
    db.refresh(users)
    return users


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(FacebookAuthUsers).offset(skip).limit(limit).all()
