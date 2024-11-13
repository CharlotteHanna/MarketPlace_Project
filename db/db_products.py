from db.models import DbProduct
from sqlalchemy.orm import Session
from schemas import ProductBase
from fastapi import HTTPException, status
from sqlalchemy import or_


#Functionality in Database

#Create product in DB
def create_product(db: Session, request: ProductBase):
    new_product = DbProduct(
            product_name=request.product_name,
            description=request.description,
            price=request.price,
            seller_id=request.seller_id,
            buyer_id=request.buyer_id,
            image_url=request.image_url,
            product_category=request.product_category,
            product_status=request.product_status
    )
        
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


#Return all products which not sold from DB
def get_all_products(db:Session):
    return db.query(DbProduct).filter(~DbProduct.product_status.ilike('sold')).all()
    


# Return products by name and description
def search_products_by_name_and_description(db:Session, key_word:str):
    search_pattern = f"%{key_word}%"
    return db.query(DbProduct).filter(
        ~DbProduct.product_status.ilike('sold'),
        or_(
        DbProduct.product_name.ilike(search_pattern),
        DbProduct.description.ilike(search_pattern)
        )
    ).all()

#Search by category
def search_products_by_category( db:Session, kew_word:str):
    search_pattern = f'%{kew_word}%'
    return db.query(DbProduct).filter(
        ~DbProduct.product_status.ilike('sold'),
        DbProduct.product_category.ilike(search_pattern)
        ).all()

    

        

 #Return  Product from DB with specifiec ID         
def get_product(db: Session, id: int):
    product = db.query(DbProduct).filter(DbProduct.product_id == id).first()
    if product is None:  
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {id} was not found")
    return product
 


#Update attributes in products table   
def update_product(db: Session, id: int, request: ProductBase):
    product = db.query(DbProduct).filter(DbProduct.product_id == id) #this is a query builder for product, not product as record. So we build product query first, and then if you want to get the record itself, then .first
    if not product.first(): #this is our record
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {id} was not found")

    product.update({
            DbProduct.product_name: request.product_name,
            DbProduct.description: request.description,
            DbProduct.price: request.price,
            DbProduct.image_url: request.image_url,
            DbProduct.product_category: request.product_category,
            DbProduct.product_status: request.product_status
        })
    db.commit()
    return {'message': f'Product with id: {id} was updated'}
    
    


#Delete Product from DB    
def delete_product(db: Session, id: int):
    product = db.query(DbProduct).filter(DbProduct.product_id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {id} was not found")
    
    db.delete(product)
    db.commit()
    return {'message': f'Product with id: {id} was deleted'}  # Return the deleted product object  






