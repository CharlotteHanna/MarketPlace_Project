
from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, Enum,Float, ForeignKey, Integer, String, Text
from db.database import Base
from sqlalchemy.orm import relationship

#  User Table
class DbUser(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True) #primary key
    username = Column(String, unique=True)  # Unique username  
    email = Column(String, unique=True)     # Unique email  
    password = Column(String)
    is_active = Column(Boolean, default=True)   #delete this attribute
    sold_product = relationship("DbProduct", primaryjoin="DbUser.user_id==DbProduct.seller_id")
    bought_product = relationship("DbProduct", primaryjoin="DbUser.user_id==DbProduct.buyer_id")
    conversations = relationship("DbConversation", back_populates="potential_buyer")
    messages = relationship("DbMessage", back_populates="sender")

# Product Table
class DbProduct(Base):
    __tablename__ = "products"
    product_id = Column(Integer, primary_key=True, index=True) #primary key
    product_name = Column(String)
    description = Column(String)
    price = Column(Integer)  # Price is in cents   
    image_url = Column(String)
    product_category = Column(String)
    product_status = Column(String)
    seller_id = Column(Integer, ForeignKey('users.user_id'))  # FK for seller
    buyer_id = Column(Integer, ForeignKey('users.user_id'), nullable=True)  # FK for buyer, allow buyer_id to be null
    seller = relationship("DbUser", foreign_keys=[seller_id], back_populates="sold_product")
    buyer = relationship("DbUser",  foreign_keys=[buyer_id], back_populates="bought_product")
    product_conversation = relationship("DbConversation",  back_populates="product")
    payments = relationship("DbPayment",  back_populates="paid_product")






# Conversation Table
class DbConversation(Base):
    __tablename__ = "conversations"
    conversation_id = Column(Integer, primary_key=True, index=True)
    potential_buyer_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)  
    desired_product_id = Column(Integer, ForeignKey("products.product_id"), nullable=True) 
    potential_buyer = relationship("DbUser", foreign_keys=[potential_buyer_id], back_populates="conversations")  
    product = relationship("DbProduct", foreign_keys=[desired_product_id], back_populates="product_conversation")
    messages = relationship("DbMessage",  back_populates="conversation")



# Message table
class DbMessage(Base):
    __tablename__ = "messages"
    message_id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("conversations.conversation_id"), nullable=True)
    sender_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    sender = relationship("DbUser",  foreign_keys=[sender_id], back_populates="messages")
    conversation = relationship("DbConversation",  foreign_keys=[conversation_id], back_populates="messages")

# Payment Table
class DbPayment(Base):
    __tablename__ = "payments"
    payment_id = Column(Integer, primary_key=True, index=True)
    paid_product_id = Column(Integer,  ForeignKey("products.product_id"))
    payment_amount = Column(Float)  # Amount paid.. change to int
    payment_status = Column(String)  # "pending", "completed", "failed"
    payment_method = Column(String)
    paid_product = relationship("DbProduct",  foreign_keys=[paid_product_id], back_populates="payments")
