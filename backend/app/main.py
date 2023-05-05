from fastapi import FastAPI
from database import models
from routers.routes import router
from database.config import engine


models.Base.metadata.create_all(bind=engine)
app = FastAPI(max_request_size=1024 * 1024 * 500)
app.include_router(router)

# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, EmailStr
# from random import randint
# from typing import Dict
# import smtplib
# from email.mime.text import MIMEText

# app = FastAPI()

# class User(BaseModel):
#     email: EmailStr
#     password: str

# users_db = {}

# def send_verification_code(email: str, code: int):
#     sender = "waqasidrees15@gmail.com" # your email address
#     password = "ihepmprpryapsums" # your email password

#     msg = MIMEText(f"Your verification code is: {code}")
#     msg['From'] = sender
#     msg['To'] = email
#     msg['Subject'] = 'Account Verification Code'

#     with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#         smtp.starttls()
#         smtp.login(sender, password)
#         smtp.send_message(msg)

# def generate_otp() -> int:
#     return randint(100000, 999999)

# def verify_otp(email: str, otp: int) -> bool:
#     if email in users_db and users_db[email]['otp'] == otp:
#         users_db[email]['verified'] = True
#         return True
#     return False

# @app.post("/signup")
# async def signup(user: User):
#     if user.email in users_db:
#         raise HTTPException(status_code=400, detail="Email already exists")

#     otp = generate_otp()
#     users_db[user.email] = {'password': user.password, 'otp': otp, 'verified': False}

#     send_verification_code(user.email, otp)

#     return {"detail": "Verification code sent to your email address"}

# @app.post("/verify")
# async def verify(email: str, otp: int):
#     if verify_otp(email, otp):
#         return {"detail": "Account verified successfully"}
#     else:
#         raise HTTPException(status_code=400, detail="Invalid OTP")

