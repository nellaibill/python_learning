from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.schemas.user_schema import User
from app.services.user_service import get_users,create_user
from app.database import SessionLocal

router = APIRouter(prefix="/users",tags=["Users"])

# Simple DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/")
def create(user:User, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/")   
def read_all(db: Session = Depends(get_db)):
   return  get_users(db)    