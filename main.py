from fastapi import FastAPI
import random
from model import Notes

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, World!"}


@app.get("/random")
def even():
    n = int(random.randint(1000, 9999))
    return {'random number': n}


@app.get("/notes")
def notes():
    return db


@app.get("/notes/{notes_id}")
def notes_detail(notes_id: int):
    notes = notes_id - 1
    return db[notes]


@app.post("/add-notes")
def add_notes(notes: Notes):
    db.append(notes.dict())
    return db[-1]


@app.delete("delete-notes/{notes_id}")
def dlt_notes(notes_id: int):
    db.pop(notes_id - 1)
    return {"task": "Deleted Successfully"}
