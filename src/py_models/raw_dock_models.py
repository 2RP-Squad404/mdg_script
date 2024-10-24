from pydantic import BaseModel
from datetime import date, datetime


# Dataset: raw_dock, Table: debit_account
class Debit_account(BaseModel):
    next_due_date: str
    delivery_address: str
    product: 'Product'
    status_description: str
    account_id: int
    due_day: int
    status_id: int
    next_real_due_date: str
    create_date: str
    properties: 'Properties'
    person_id: int
    production_date: date


class Product(BaseModel):
    issuer_account_number: str
    issuer_bank_number: int
    issuer_branch_number: str
    product_id: int
    product_type: str
    produto_description: str


class Properties(BaseModel):
    cmd_seq: int
    dt_capture: str
    dt_publish: str
    dt_sync: str
    dt_transaction: str
    issuer_id: int
    issuer_name: str
    operation: str




# Dataset: raw_dock, Table: debit_person
class Debit_person(BaseModel):
    bank_account: str
    bank_agency: str
    bank_code: int
    birth_date: str
    birth_place: str
    document_id: str
    document_issuer: str
    email: str
    father: str
    gender: str
    graduation_degree: str
    mother: str
    name: str
    nationality: str
    occupation: str
    person_id: int
    person_type: str
    politically_exposed: bool
    properties: 'Properties'
    salary: float
    spouse_name: str
    spouse_salary: float
    tax_identification_number: str
    production_date: date


class Properties(BaseModel):
    cmd_seq: int
    dt_capture: str
    dt_publish: str
    dt_sync: str
    dt_transaction: str
    issuer_id: int
    issuer_name: str
    operation: str


