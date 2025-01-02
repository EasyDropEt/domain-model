```py
from datetime import datetime
from enum import StrEnum
from typing import TypedDict
from uuid import UUID


class WayPointAction(StrEnum):
    PICKUP = "PICKUP"
    DROP_OFF = "DROP_OFF"


class WayPoint(TypedDict):
    order_id: UUID
    action: WayPointAction
    location_id: UUID
    eta: datetime
    sequence: int


class Route(TypedDict):
    waypoints: list[WayPoint]
    estimated_distance_in_kms: float
    estimated_time_in_minutes: int
```

```json
{
    "waypoints": [
        {
            "order_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "action": "PICKUP",
            "location_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "eta": "2025-01-02T07:04:22.746Z",
            "sequence": 0
        }
    ],
    "estimated_distance_in_kms": 0,
    "estimated_time_in_minutes": 0
}
```
