from typing import List
from fastapi import APIRouter, Depends
from schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_users
from auth.oauth2 import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

#Use Create User functionality from db_users file
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
        return db_users.create_user(db, request)

#Use read User functionality from db_users file

      #return all users
@router.get('/', response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
        return db_users.get_all_users(db)
 

      #return User with conditions
@router.get('/{id}', response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
        
        return db_users.get_user(db, id)
       


#Use Update User functionality from db_users file
@router.post('/{id}')
def update_user(id: int, request: UserBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
        return db_users.update_user(db, id, request)
 

#Use Delete User functionality from db_users file
@router.delete('/{id}')
def delete_user(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
        return db_users.delete_user(db, id)