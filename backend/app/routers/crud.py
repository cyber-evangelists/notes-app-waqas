from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from database.models import Notes, ClientData, MyUser
from schema.schemas import NotesSchema, RequestLoginMyUser, MyUserSchema, LoginMyUserSchema
import requests
from random import randint
from typing import Dict
import smtplib
from email.mime.text import MIMEText
from sqlalchemy import text


def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Notes).offset(skip).limit(limit).all()


def get_notes_by_id(db: Session, notes_id: int):
    return db.query(Notes).filter(Notes.id == notes_id).first()


def create_notes(db: Session, notes: NotesSchema):
    notes = Notes(
        title=notes.title,
        description=notes.description,
        check_in=notes.check_in,
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


def create_client(db: Session, access_token: str):
    url = f"https://graph.facebook.com/v16.0/me?fields=id%2Cname%2Cemail&access_token={access_token}"
    response = requests.get(url)
    user = response.json()
    user = ClientData(
        name=user["name"],
        email=user["email"],
        access_token=access_token,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ClientData).offset(skip).limit(limit).all()


def Create_my_user(db: Session, my_user: MyUserSchema,):
    my_user = MyUser(
        # username = my_user.username,
        email = my_user.email,
        password = my_user.password,
    )
    
    db.add(my_user)
    db.commit()
    db.refresh(my_user)
    return my_user


def get_my_user(db: Session, my_user: LoginMyUserSchema):
    return db.query(MyUser).filter(MyUser.email == my_user.email and MyUser.password == my_user.password).first()



def send_verification_code(email: str, code: int):
    sender = "waqasidrees15@gmail.com"
    password = "ihepmprpryapsums"

    msg = MIMEText(f"Your verification code is: {code}")
    msg['From'] = sender
    msg['To'] = email
    msg['Subject'] = 'Account Verification Code'

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender, password)
        smtp.send_message(msg)


def generate_otp() -> int:
    return randint(100000, 999999)


def verify_otp(email: str, otp: int, db: Session) -> bool:
    if db.query(MyUser).filter(MyUser.email == email and MyUser.otp == otp):
        db.query(MyUser).filter(MyUser.verified) == True
        return True
    return False

def get_my_user(db: Session, skip: int = 0, limit: int = 100):
    return db.query(MyUser).offset(skip).limit(limit).all()