from fastapi import FastAPI
from db.database import engine
from db import models
from routers import conversations, messages, payments, products, users, categories
from auth import authentication

# from auth import authentication
# import logging  


# logging.basicConfig(level=logging.INFO)  
app = FastAPI()
app.include_router(authentication.router)
app.include_router(users.router)
app.include_router(categories.router)
app.include_router(products.router)
app.include_router(conversations.router)
app.include_router(messages.router)
app.include_router(payments.router)

# app.include_router(authentication.router)





# Create the database tables  
models.Base.metadata.create_all(engine)







