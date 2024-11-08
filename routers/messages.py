from fastapi import APIRouter, Depends
from schemas import MessageBase, MessageDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_messages



router = APIRouter(
 prefix='/messages',
 tags=['messages']
)



#Use Create Message functionality from db_messages file
@router.post('/', response_model=MessageDisplay)
def create_message(request: MessageBase, db: Session = Depends(get_db)):
    return db_messages.create_message(db, request)



#Use Delete Message functionality from db_messages file
@router.delete('/{id}')
def delete_message(id: int, db: Session = Depends(get_db)):
    return db_messages.delete_message(db, id)
