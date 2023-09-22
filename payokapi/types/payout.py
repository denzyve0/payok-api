from .base import PayOkType
from ..enums import Methods, Status

from datetime import date

class Payout(PayOkType):
    payout_id: int
    method: Methods
    amount: float
    comission_percent: float
    comission_fixed: float
    amount_profit: float
    date_create: date
    date_pay: date
    status: Status
