from fastapi import FastAPI
from database import models
from routers.routes import router
from database.config import engine


models.Base.metadata.create_all(bind=engine)
app = FastAPI(max_request_size=1024 * 1024 * 500)
app.include_router(router)
