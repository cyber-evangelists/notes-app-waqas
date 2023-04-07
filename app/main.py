from fastapi import FastAPI
import database.models
from routers.routes import router
from database.config import engine


database.models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(router, prefix="/notes", tags=["notes"])

