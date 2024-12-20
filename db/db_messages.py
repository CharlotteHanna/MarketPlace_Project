from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from db.models import DbMessage, DbConversation
from schemas import MessageBase





#Functionality in Database

#Create message in DB
def create_message(db:Session, request: MessageBase):
#  exist_conversation = db.query(DbConversation).filter(DbConversation.id==request.conversation_id).first()
#  if not exist_conversation:
#   call create_conversation from db_conversation
 
   new_message = DbMessage(
      conversation_id=request.conversation_id,
      sender_id = request.sender_id,
      content =request.content
 )
   db.add(new_message)
   db.commit()
   db.refresh(new_message)
   return new_message

# def get_messages_by_conversation(db:Session, conversation_id:int):
#  conversation =db.query(DbConversation).filter(DbConversation.id==conversation_id).first()
#  if not conversation:
#   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail ="Conversation not found")
 
#  messages = db.query(DbMessage).filter(DbMessage.conversation_id==conversation_id).order_by(DbMessage.timestamp).all()
#  return messages


# def get_message_by_id(db:Session, message_id:int):
#  message = db.query(DbMessage).filter(DbMessage.id ==message_id).first()
#  if not message:
#   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail ="Message not found")
#  return message


#Delete Message from DB
def delete_message(db: Session, id: int):
 message = db.query(DbMessage).filter(DbMessage.message_id==id).first()
 if not message:
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Message with id {id} was not found')
 
 db.delete(message)
 db.commit()
 return {'message': f'Message with id: {id} was deleted'}



