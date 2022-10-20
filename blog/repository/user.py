from fastapi import status,HTTPException
from typing import List
import schemas,models
from sqlalchemy.orm import Session
from hashing import Hash

def create(request: schemas.User, db: Session):
    # hashed_password= pwd_cxt.hash(request.password) (or we can ake an another file having class )
    # new_user = models.User(request)
    new_user = models.User(name = request.name, email = request.email, password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_one(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'user with id {id} not found.')
    
    return user

def get_all(db: Session):
    users = db.query(models.User).all()
    return users

def destroy(id: int, db: Session):
    user= db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'blog with id {id} not found.')

    user.delete(synchronize_session=False)
    db.commit()
    return {'deatil': f'user with id {id} has been deleted succesfully.'}