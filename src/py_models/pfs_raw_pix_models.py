from pydantic import BaseModel
from datetime import date, datetime


# Dataset: pfs_raw_pix, Table: v_dict_direto
class V_dict_direto(BaseModel):
    production_date: date
    account: 'Account'
    clearingAcknowledgeTimestampUtc: str
    clearingEndClaimTimestampUtc: str
    confirmationToken: str
    holder: 'Holder'
    key: 'Key'
    newStatus: 'Newstatus'
    newStatusUtcTimestamp: str
    reason: str


class Account(BaseModel):
    branch: str
    accountNumber: str
    accountType: str
    openingDate: str


class Holder(BaseModel):
    name: str
    tradeName: str
    taxId: str


class Key(BaseModel):
    id: str
    value: str
    type: str


class Newstatus(BaseModel):
    id: int
    description: str


