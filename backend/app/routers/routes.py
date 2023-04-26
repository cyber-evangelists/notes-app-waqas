from fastapi import APIRouter, Depends, File, UploadFile
from database.config import SessionLocal
from sqlalchemy.orm import Session
from schema.schemas import Response, RequestNotes, RequestUsers
from routers import crud


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create")
async def create_notes_service(request: RequestNotes, db: Session = Depends(get_db)):
    crud.create_notes(db, notes=request.parameter)
    return Response(status="Ok", code="200", message="Notes created successfully").dict(
        exclude_none=True 
    )


@router.get("/")
async def get_notses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    notes = crud.get_notes(db, skip, limit)
    return Response(
        status="Ok", code="200", message="Success fetch all data", result=notes
    )


@router.patch("/update")
async def update_notes(request: RequestNotes, db: Session = Depends(get_db)):
    notes = crud.update_notes(
        db,
        notes_id=request.parameter.id,
        title=request.parameter.title,
        description=request.parameter.description,
    )
    return Response(
        status="Ok", code="200", message="Success update data", result=notes
    )


@router.delete("/delete")
async def delete_notes(request: RequestNotes, db: Session = Depends(get_db)):
    crud.remove_notes(db, notes_id=request.parameter.id)
    return Response(status="Ok", code="200", message="Success delete data").dict(
        exclude_none=True
    )


@router.post('auth/facebook')
async def create_notes_service(request: RequestUsers, db: Session = Depends(get_db)):
    crud.create_users(db, notes=request.parameter)
    return Response(status="Ok", code="200", message="Notes created successfully").dict(
        exclude_none=True 
    )