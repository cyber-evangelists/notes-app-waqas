from fastapi import FastAPI
import models
from routes import router
from config import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# app.include_router(router, prefix="/book", tags=["book"])


@app.post("/create-notes")
def create_notes(details: ):
    


# @app.post("/add-notes")
# def notes(details: CreateNotesRequest, db: Session = Depends(get_db)):
#     created = model.Notes(id = details.id, title =  details.title, description = details.description, url = details.url)
#     db.add(created)
#     db.commit()
#     return {
#         "success": True,
#         "created_id": created.id
#     }


# @app.get("/notes/{notes_id}")
# def notes_detail(notes_id: int, db: Session = Depends(get_db)):
#     return db.query(model.Notes).filter(model.Notes.notes_id == notes_id).first()


# @app.post("/add-notes")
# def add_notes(notes: Notes):
#     db.append(notes.dict())
#     return db[-1]


# @app.delete("delete-notes/{notes_id}")
# def dlt_notes(notes_id: int):
#     db.pop(notes_id - 1)
#     return {"task": "Deleted Successfully"}
