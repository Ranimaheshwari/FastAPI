from sqlalchemy.orm import Session
import schemas,models
from fastapi import status, HTTPException, Response

def get_all(db: Session):
    blogs = db.query(models.Book).all()
    return blogs

def create(request : schemas.Book, db : Session):
    new_blog = models.Book(title=request.title,author_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_one(id: int, response : Response, db: Session):
    blog = db.query(models.Book).filter(models.Book.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'blog with the {id} is not available.'}
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'blog with the {id} is not available.')

    return blog

def destroy(id:int , db : Session):
    blog= db.query(models.Book).filter(models.Book.id == id)
    if not blog.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'blog with id {id} not found.')

    blog.delete(synchronize_session=False)
    db.commit()
    return {'deatil': f'the blog with id {id} has been deleted succesfully.'}

def update(id:int , request: schemas.Book, db: Session):
    blog = db.query(models.Book).filter(models.Book.id == id)
    
    if not blog.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail= f'blog with id {id} not found') 
    
    blog.update({'title':'updated title','body':'updated body'})

    # blog.update(request)
    db.commit()
    return {'deatil': f'the blog with id {id} has been updated succesfully.'}
