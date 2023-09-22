from .base import PayOkType
from ..enums import Currency, Methods

from datetime import date

class Transaction(PayOkType):
    transaction: int
    email: str
    amount: float
    currency: Currency
    comission_percent: float
    comission_fixed: float
    amount_profit: float
    method: Methods
    payment_id: int
    description: str
    date: date
    pay_date: date
    transaction_status: int
    custom_fields: str
    webhook_status: int
    webhook_amount: int
