from typing import List
from fastapi import APIRouter, Depends, FastAPI, Request, Response, status, HTTPException
from .. import schemas, database, models
from .. database import SessionLocal
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/blog",
    tags=['Blog']


)

get_db = database.get_db

@router.get("/", response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    new_blog = models.Blog(title=request.title, body=request.body,user_id=1 )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id) # .delete(synchronize_session=False)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"done"}
    

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    # blog.update(request)
    # db.commit()
    # db.refresh(blog)
    return {"put request Successfully Completed"}

@router.get("/{id}", status_code = 200)
def show(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first() 
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Provided ID: {id}, is not Available.")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {f"Provided ID: {id}, is not Available."}
    return blog
