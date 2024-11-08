
from typing import List
from fastapi import APIRouter, Depends
from db import db_payments
from db.database import get_db
from schemas import PaymentsDisplay, PaymentsBase
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/payments',
    tags=['payments']
)




#Use Create Payment functionality from db_payments file
@router.post('/', response_model=PaymentsDisplay)
def create_payment(request: PaymentsBase, db: Session = Depends(get_db)):
    return db_payments.create_payment(db, request)

#Use read Payment functionality from db_payments file

    #return all payments
@router.get('/', response_model=List[PaymentsDisplay])
def get_all_payments(db: Session = Depends(get_db)):
    return db_payments.get_all_payments(db)

    #return payments with conditions
@router.get('/{id}', response_model=PaymentsDisplay)
def get_payment(id: int, db: Session = Depends(get_db)):
    return db_payments.get_payment(db, id)

#Use Update Payment functionality from db_payments file
@router.post('/{id}')
def update_payment(id: int,request: PaymentsBase, db: Session = Depends(get_db)):
    return db_payments.update_payment(db, id, request)

#Use Delete Payment functionality from db_payments file
@router.delete('/{id}')
def delete_payment(id: int, db: Session = Depends(get_db)):
    return db_payments.delete_payment(db, id)
