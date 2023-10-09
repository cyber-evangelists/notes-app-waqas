from fastapi import APIRouter, Depends, HTTPException
from database import config, models
from sqlalchemy.orm import Session
from schema.schemas import Response, RequestNotes, RequestClientData, NotesResponse, ClientDataResponse, RequestMyUser, RequestLoginMyUser, MyUserSchema
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


@router.post("/notes/create", response_model=NotesResponse)
async def create_notes_service(request: RequestNotes, db: Session = Depends(get_db)):
    crud.create_notes(db, notes=request.parameter)
    return Response(message="Notes created successfully").dict(
        exclude_none=True
    )


@router.get("/notes")
async def get_notses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    notes = crud.get_notes(db, skip, limit)
    return Response(result=notes)


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
        result=notes
    )


@router.delete("/notes/delete")
async def delete_notes(request: RequestNotes, db: Session = Depends(get_db)):
    crud.remove_notes(db, notes_id=request.parameter.id)
    return Response(message="Success delete data").dict(
        exclude_none=True
    )


@router.post('/login/facebook', response_model=ClientDataResponse)
async def create_client_service(request: RequestClientData, db: Session = Depends(get_db)):
    crud.create_client(db, access_token=request.parameter.access_token)
    return Response(message="User created successfully").dict(
        exclude_none=True
    )


@router.get("/users")
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    user = crud.get_user(db, skip, limit)
    return Response(
        message="Success fetch all data", result=user
    )


# @router.post("/register")
# async def create_my_user_service(request: RequestMyUser, db: Session = Depends(get_db)):
#     crud.Create_my_user(db, my_user=request.parameter)
#     otp = crud.generate_otp()

#     crud.send_verification_code(request.parameter.email, otp)

#     return {"detail": "Verification code sent to your email address"}


@router.post("/signup")
async def signup(user: MyUserSchema, db: Session = Depends(get_db)):
    otp = crud.generate_otp()
    crud.send_verification_code(user.email, otp)
    user = models.MyUser(
        email = user.email,
        password = user.password,
        otp = otp,
        verified = False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"detail": "Verification code sent to your email address"}


@router.post("/login")
async def login_user(request: RequestLoginMyUser, db:Session = Depends(get_db)):
    my_user = crud.get_my_user(db, my_user=request.parameter)
    return Response(message="Login Successfully", result=my_user)


@router.post("/verify")
async def verify(email: str, otp: int, db: Session = Depends(get_db)):
    if crud.verify_otp(email, otp, db):
        return {"detail": "Account verified successfully"}
    else:
        raise HTTPException(status_code=400, detail="Invalid OTP")
    
    
    
    
@router.get("/my-users")
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    user = crud.get_my_user(db, skip, limit)
    return Response(
        message="Success fetch all data", result=user
    )
