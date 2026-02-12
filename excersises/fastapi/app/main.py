from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)
