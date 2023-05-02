from fastapi import APIRouter, Depends
from database import config
from sqlalchemy.orm import Session
from schema.schemas import Response, RequestNotes
from routers import crud
import sys


sys.setrecursionlimit(3000)

router = APIRouter()

def get_db():
    db = config.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/notes/create")
async def create_notes_service(request: RequestNotes, db: Session = Depends(get_db)):
    crud.create_notes(db, notes=request.parameter)
    return Response(status="Ok", code="200", message="Notes created successfully").dict(
        exclude_none=True
    )


@router.get("/notes")
async def get_notses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    notes = crud.get_notes(db, skip, limit)
    return Response(
        status="Ok", code="200", message="Success fetch all data", result=notes
    )


@router.patch("/notes/update")
async def update_notes(request: RequestNotes, db: Session = Depends(get_db)):
    notes = crud.update_notes(
        db,
        notes_id=request.parameter.id,
        title=request.parameter.title,
        description=request.parameter.description,
        check_in=request.parameter.check_in,
    )
    return Response(
        status="Ok", code="200", message="Success update data", result=notes
    )


@router.delete("/notes/delete")
async def delete_notes(request: RequestNotes, db: Session = Depends(get_db)):
    crud.remove_notes(db, notes_id=request.parameter.id)
    return Response(status="Ok", code="200", message="Success delete data").dict(
        exclude_none=True
    )


@router.post('/login/facebook')
async def create_client_service(access_token: str, db: Session = Depends(get_db)):
    crud.create_client(db, access_token=access_token)
    user = crud.get_user(db)[-1]
    return Response(status="Ok", code="200", message="User created successfully", result={"id": user.id, "name": user.name, "email": user.email}).dict(
        exclude_none=True
    )


@router.get("/users")
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    user = crud.get_user(db, skip, limit)
    return Response(
        status="Ok", code="200", message="Success fetch all data", result=user
    )
