from fastapi import FastAPI, File, UploadFile
import database.models
from routers.routes import router
from database.config import engine
from database import models 
from fastapi import APIRouter, Depends, File, UploadFile
from database.config import SessionLocal
from sqlalchemy.orm import Session
from schema.schemas import Response, RequestNotes
from sqlalchemy.orm import Session
from database.models import Notes
from schema.schemas import NotesSchema
from sqlalchemy import BINARY
from datetime import datetime
from fastapi import UploadFile, File
import os
from routers import routes
import requests


database.models.Base.metadata.create_all(bind=engine)
app = FastAPI(max_request_size=1024 * 1024 * 500)
app.include_router(router, prefix="/notes", tags=["notes"],)


# curl = "https://graph.facebook.com/v16.0/me?fields=id%2Cname%2Ctoken_for_business&access_token=EAASPaTEoZANoBABTrsTaDXqT5bp5BDjSxgYe1UIystNytzqt2jDxUZBcpvZAVXxZCTwm3aEImFzGI4JSas6Tsj0j3xQPiCmvh6YxtPavx4OEUkDTcAZCxdvIaOqTgSdrk8fVbqtgOZBYDOSi3ywu1Dc2xwVZBBnVR8vudZC19etESRmIj8uDAMaqe4Nr4LkZBYtk5ldxZC4pYC46lNNIYpoQUt"
# response = requests.get(curl)
# print(response.text)
