from fastapi import APIRouter, HTTPException
from .. import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from .. hashing import Hash
from .. repository import user

get_db = database.get_db
router = APIRouter(
    prefix="/user",
    tags=['User']
)

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User,db: Session = Depends(get_db)):
    return user.create(request,db)
    

# GET USERS
@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id,db)
    