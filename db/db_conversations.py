from schemas import ConversationBase
from sqlalchemy.orm.session import Session
from db.models import DbConversation
from fastapi import HTTPException, status




#Functionality in Database

#Create conversation in DB
def create_conversation(db: Session, request: ConversationBase):
    # think how to combine conversation and messages creation but we need to check existing conversation by product_id and conversation_id and potential_buyer_id
    existing_conversation =db.query(DbConversation).filter(
            DbConversation.desired_product_id==request.desired_product_id).first()

    if existing_conversation:
        return existing_conversation
 
    new_conversation = DbConversation(
    potential_buyer_id = request.potential_buyer_id,
    desired_product_id = request.desired_product_id
    )

    db.add(new_conversation)
    db.commit()
    db.refresh(new_conversation)
    return new_conversation

#Return all Conversations from DB
def get_all_conversations(db: Session):
 return db.query(DbConversation).all()



#Return  Conversation from DB with specifiec ID
def get_conversation_by_id(db: Session, id: int):
 conversation = db.query(DbConversation).filter(DbConversation.conversation_id==id).first()
 if not conversation:
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =f'Conversation with id: {id} was not found')
 return conversation


#Delete Conversation from DB
def delete_conversation(id: int, db: Session):
 conversation = db.query(DbConversation).filter(DbConversation.conversation_id==id).first()
 if not conversation:
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =f'Conversation with id {id} not found')
 db.delete(conversation)
 db.commit()
 return {'message': f'Conversation with id: {id} was deleted'}
 
