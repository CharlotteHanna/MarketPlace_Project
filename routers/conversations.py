from fastapi import APIRouter, Depends
from schemas import ConversationBase, ConversationDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_conversations
from typing import List

router = APIRouter(
    prefix='/conversations',
    tags=['conversations']
)

#Use Create Conversation functionality from db_conversations file
@router.post('/', response_model=ConversationDisplay)
def start_conversation(request: ConversationBase, db: Session = Depends(get_db)):
   return db_conversations.create_conversation(db, request)

#Use read Conversation functionality from db_conversations file

    #return all conversations
@router.get('/',response_model=List[ConversationDisplay])
def get_all_conversations(db: Session = Depends(get_db)):
      return db_conversations.get_all_conversations(db)
    
    
    #return Conversations with conditions
@router.get('/{id}',response_model=ConversationDisplay)
def get_conversation(id: int, db: Session = Depends(get_db)):
  return db_conversations.get_conversation_by_id(db,id) 
  
#Use Delete Conversation functionality from db_conversations file
@router.delete('/{id}')
def delete_conversation(id: int, db: Session = Depends(get_db)):
   return db_conversations.delete_conversation(id, db)
  

