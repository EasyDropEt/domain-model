## Cunsumer

```py
from typing import TypedDict
from uuid import UUID


class Consumer(TypedDict):
    id: UUID
    name: str
    phone_number: str
    email: str
    active_status: bool
    notification_ids: list[UUID]
```

```json
{
  "id": "00000000-0000-0000-0000-000000000004",
  "name": "Alice Johnson",
  "role": "consumer",
  "phone_number": "+6543219870",
  "email": "alice.johnson@example.com",
  "active_status": true,
  "notification_ids": ["00000000-0000-0000-0000-000000000004", "00000000-0000-0000-0000-000000000004"]
}
```
