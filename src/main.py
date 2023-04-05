from fastapi import FastAPI, Depends
import random
from .model import Notes
from .schemas import CreateNotesRequest
from sqlalchemy.orm import Session
from .database import get_db

app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Hello, World!"}


# @app.get("/random")
# def even():
#     n = int(random.randint(1000, 9999))
#     return {'random number': n}


@app.post("/add-notes")
def notes(details: CreateNotesRequest, db: Session = Depends(get_db)):
    created = Notes(id = details.id, title =  details.title, description = details.description, url = details.url)
    db.add(created)
    db.commit()
    return {
        "success": True,
        "created_id": created.id
    }


@app.get("/notes/{notes_id}")
def notes_detail(notes_id: int, db: Session = Depends(get_db)):
    return db.query(Notes).filter(Notes.notes_id == notes_id).first()


# @app.post("/add-notes")
# def add_notes(notes: Notes):
#     db.append(notes.dict())
#     return db[-1]


# @app.delete("delete-notes/{notes_id}")
# def dlt_notes(notes_id: int):
#     db.pop(notes_id - 1)
#     return {"task": "Deleted Successfully"}
