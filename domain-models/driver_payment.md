## Driver Payment

```py
from datetime import datetime
from enum import StrEnum
from typing import TypedDict


class PaymentMethod(StrEnum):
    BANK_TRANSFER = "BANK_TRANSFER"
    TELEBIRR = "TELEBIRR"


class DriverPayment(TypedDict):
    amount: float
    status: str
    date: datetime
    payment_method: PaymentMethod
```

```json
{
    "amount": 0,
    "status": "string",
    "date": "2025-01-01T08:21:18.100Z",
    "payment_method": "BANK_TRANSFER"
}
```
