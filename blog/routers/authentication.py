from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models, token
from sqlalchemy.orm import Session
from .. hashing import Hash
# from .. import token
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
import jose

router = APIRouter(
    tags = ['Authentication']
)


@router.post("/login")
def login(request:schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
    # Generate JWT Token and return
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

