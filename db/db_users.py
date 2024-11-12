from sqlalchemy.orm import Session
from db.hash import Hash
from schemas import UserBase
from db.models import DbUser
from fastapi import HTTPException, status


#Functionality in Database

#Create user in DB
def create_user(db: Session, request: UserBase):
        existing_user = db.query(DbUser).filter(DbUser.username == request.username).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already taken")

        new_user = DbUser(
            username=request.username,
            email=request.email,
            password=Hash.bcrypt(request.password)
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
           

#Return all users from DB   
def get_all_users(db: Session):
    return db.query(DbUser).all()
    
#Return user from DB with specific ID 
def get_user(db: Session, user_id: int):
    user = db.query(DbUser).filter(DbUser.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} was not found")
    return user

def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with username {username} not found")
    return user

#Update attributes in users table
def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.user_id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} was not found")

   
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)
        })
    db.commit()
    return {'message': f'User with id: {id} was updated'}
   

#Delete user from DB  
def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.user_id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} was not found")
    
    db.delete(user)
    db.commit()
    return {'message': f'User with id: {id} was deleted'}
  