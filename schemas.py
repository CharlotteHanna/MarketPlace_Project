
from datetime import datetime
from typing import Annotated, List, Literal
from fastapi import Body
from pydantic import BaseModel







### User ###
# Base schema for users
class UserBase(BaseModel):
    username: str
    email: str
    password: str  # Should be hashed before storing
    


# Schema for displaying a user
class UserDisplay(BaseModel):
    user_id: int
    username: str
    email: str
    class Config:
        orm_mode = True


### Category ###
# Base schema for categories
class CategoryBase(BaseModel):
    category_name: str

# Schema for displaying a category 
class CategoryDisplay(BaseModel):
    category_name: str
    class Config:
        orm_mode = True
        



### Product ###
# Base schema for products
class ProductBase(BaseModel):
    product_name: Annotated[str, Body(min_length= 5, max_length= 25)]
    description: Annotated[str, Body(min_length= 5, max_length= 500)]
    price: Annotated[int, Body(gt=0)]
    image_url: Annotated[str, Body(min_length= 5)]
    product_category_id: int
    product_status: str
    seller_id: int
    buyer_id: int



# Schema for displaying a product  
class ProductDisplay(BaseModel):
    product_id: int
    product_name: str
    description: str
    price: int
    image_url: str
    product_category: CategoryDisplay
    product_status: str
    seller: UserDisplay
    class Config:
        orm_mode = True
        

# class Message inside ConversationDisplay
class Message(BaseModel):
    timestamp: datetime
    sender_id: int
    content: str
    class Config:
        orm_mode = True




### Conversation ###
# Base schema for conversation
class ConversationBase(BaseModel):
    desired_product_id: int
    potential_buyer_id: int
    # sender :Sender 


# Schema for displaying a payment 
class ConversationDisplay(BaseModel):
    conversation_id: int
    desired_product_id:int
    potential_buyer_id:int
    messages: List[Message] = []
    #seller_name
    # buyer_name
    
    class Config:
        orm_mode = True
        


### Messages ###
# Base schema for Messages
class MessageBase(BaseModel):
    content: str
    conversation_id: int
    sender_id: int

# Schema for displaying a message 
class MessageDisplay(BaseModel):
    message_id: int
    timestamp: datetime
    sender_id: int
    conversation_id: int
    content: str

    class Config:
        orm_mode = True




### Payments ###
# Base schema for payments
class PaymentsBase(BaseModel):
    paid_product_id: int
    payment_amount: int
    payment_status: str
    payment_method: str
    


# Schema for displaying a payment 
class PaymentsDisplay(BaseModel):
    payment_id: int
    paid_product_id: int
    payment_amount: int
    payment_status: str
    payment_method: str
    

    class Config:
        orm_mode = True
        
    

   
    
 