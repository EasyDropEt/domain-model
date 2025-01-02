```py
from datetime import datetime
from enum import StrEnum
from typing import NotRequired, TypedDict
from uuid import UUID

from src.domain.entities.driver_payment import DriverPayment
from src.domain.entities.route import Route


class DeliveryJobStatus(StrEnum):
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    FAILED = "failed"


class DeliveryJob(TypedDict):
    id: UUID
    order_ids: list[UUID]
    route: Route
    driver_id: NotRequired[UUID]
    driver_payment: NotRequired[DriverPayment]
    status: DeliveryJobStatus
    estimated_payment: float
    estimated_completion_time: datetime
```

```json
{
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "order_ids": [
      "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    ],
    "route": {
      "waypoints": [
        {
          "location_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
          "eta": "2025-01-01T08:21:18.100Z",
          "sequence": 0
        }
      ]
    },
    "driver_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "driver_payment": {
      "amount": 0,
      "status": "string",
      "date": "2025-01-01T08:21:18.100Z",
      "payment_method": "BANK_TRANSFER"
    },
    "status": "in_progress",
    "estimated_payment": 0,
    "estimated_completion_time": "2025-01-01T08:21:18.100Z"
  }
```
