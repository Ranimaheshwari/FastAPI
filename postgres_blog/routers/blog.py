from fastapi import APIRouter,Depends, status, Response
from typing import List
from .. import schemas,database,oauth2
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
    )

get_db = database.get_db

@router.get("/", response_model= List[schemas.ShowBlog])
def all_blog(db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.post("/",status_code=status.HTTP_201_CREATED)
def create(request : schemas.Blog,db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request,db)


@router.get("/{id}",status_code=200, response_model=schemas.ShowBlog, tags=["Blogs"])
def show(id: int, response : Response, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_one(id,response,db)


@router.delete("/delete/{id}",status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)

@router.put("/{id}",status_code= status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)
    

