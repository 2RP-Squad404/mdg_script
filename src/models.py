# Este arquivo possui os modelos das tabelas que serão usados para criação dos dados mockados
from datetime import datetime
from typing import Any
from pydantic import BaseModel

class Campaigns(BaseModel):
    acess_number: Any
    id_campaign: Any
    type_campaign: str
    days_valid: Any
    data_campaign: datetime
    channel: str
    return_status: str
    return_date: datetime
    client_id: str
class Purchases(BaseModel):
    purchase_id: str
    product_name: str
    product_id: str
    amount: Any
    price: Any
    discount_applied: Any
    payment_method: str
    purchase_datetime: datetime
    purchase_location: str
    client_id: str
