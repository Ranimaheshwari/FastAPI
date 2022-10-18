from fastapi import APIRouter,Depends, status
from typing import List
import schemas,database
from sqlalchemy.orm import Session
from repository import user

router = APIRouter(
    prefix= "/user",
    tags=['Users']
    )
get_db = database.get_db


@router.post("/", response_model= schemas.ShowUSer)
def create_user(request: schemas.User, db: Session = Depends(get_db) ):
    return user.create()

@router.get("/{id}", response_model= schemas.ShowUSer)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_one(id,db)

@router.get("/", response_model= List[schemas.ShowUSer])
def all_users(db: Session = Depends(get_db)):
    return user.get_all(db)

@router.delete("/delete/{id}",status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return user.destroy(id,db)