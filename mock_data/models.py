from pydantic import BaseModel

class Person(BaseModel):
    person_id: int 
    name: str
    email: str 
    gender: str
    birth_date: str
    address: str
    salary: float
    cpf: str
    
class Account(BaseModel):
    account_id: int
    status_id: int 
    due_day: int
    person_id: int
    balance: float
    available_balance: float 
    
class Card(BaseModel):
    card_id: int
    card_number: str
    account_id: int
    status_id: int
    limit: float
    expiration_date: str
    
class BuyEvent():
    person_id: int 
    name: str
    email: str 
    address: str
    salary: float
    cpf: str
    card_id: int
    card_number: str
    account_id: int
    status_id: int
    limit: float
    expiration_date: str
    

    
    
    
    
    