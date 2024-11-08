from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from db.models import DbPayment
from schemas import PaymentsBase


#Functionality in Database

#Create payment in DB
def create_payment(db: Session, request: PaymentsBase):
    new_payment = DbPayment(
        payment_amount = request.payment_amount,
        payment_status = request.payment_status,
        payment_method = request.payment_method,
        paid_product_id = request.paid_product_id
    )
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return new_payment


#Return all Payments from DB
def get_all_payments(db: Session):
    return db.query(DbPayment).all()


#Return  Payment from DB with specifiec ID
def get_payment(db: Session, id: int):
    payment = db.query(DbPayment).filter(DbPayment.payment_id == id).first()
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Payment with id: {id} was not found')
    return payment



#Update attributes in payments table
def update_payment(db: Session, id: int, request: PaymentsBase):
    payment = db.query(DbPayment).filter(DbPayment.payment_id == id)
    if not payment.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Payment with id: {id} was not found')
    
    payment.update({
        DbPayment.payment_amount: request.payment_amount,
        DbPayment.payment_method: request.payment_method,
        DbPayment.payment_status: request.payment_status
        })
    db.commit()
    return {'message': f'Payment with id: {id} was updated'}


#Delete Payment from DB
def delete_payment(db: Session, id: int):
    payment = db.query(DbPayment).filter(DbPayment.payment_id == id).first()
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Payment with id: {id} was not found')
    
    db.delete(payment)
    db.commit()
    return {'message': f'Payment with id: {id} was deleted'}