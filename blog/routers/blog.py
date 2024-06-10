from typing import List
from fastapi import APIRouter, Depends, FastAPI, Request, Response, status, HTTPException
from .. import schemas, database, models
from .. database import SessionLocal
from sqlalchemy.orm import Session
from .. repository import blog
from .. repository import user
from .. import oauth2

router = APIRouter(
    prefix="/blog",
    tags=['Blog']


)

get_db = database.get_db

@router.get("/", response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db),currect_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db),currect_user: schemas.User = Depends(oauth2.get_current_user)):
    blog.create(request,db)
   


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db),currect_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id,db)
    
    

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Blog, db: Session = Depends(get_db),currect_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)
    

@router.get("/{id}", status_code = 200, response_model=schemas.ShowBlog)
def show(id:int, db: Session = Depends(get_db),currect_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id,db)
    