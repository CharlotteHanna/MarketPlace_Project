from typing import List  
from fastapi import APIRouter, Depends
from schemas import ProductBase, ProductDisplay, UserBase
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_products
from auth.oauth2 import get_current_user

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

#Use Create Product functionality from db_products file
@router.post('/', response_model=ProductDisplay)
def create_product(request: ProductBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
        return db_products.create_product(db, request)
    

#Use read Product functionality from db_products file
        #return all products
@router.get('/', response_model=List[ProductDisplay])
def get_all_products(db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
        return db_products.get_all_products(db)
   


        #return products with conditions
@router.get('/{id}', response_model=ProductDisplay)
def get_product(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
        return db_products.get_product(db, id)
   
     

#Use Update Product functionality from db_products file
@router.post('/{id}')
def update_product(id: int, request: ProductBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
        return db_products.update_product(db, id, request)
  

#Use Delete Product functionality from db_products file
@router.delete('/{id}')
def delete_product(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
        return db_products.delete_product(db, id)
   