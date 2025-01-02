## Order

```py

class ParcelSize(enum.StrEnum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


class ParcelDimensions(TypedDict):
    length: int
    width: int
    height: float


class Parcel(TypedDict):
    size: ParcelSize
    weight: float
    dimensions: ParcelDimensions
    fragile: bool

class Order(TypedDict):
    id: str
    consumer: Consumer
    business_id: str
    bill_id: str
    latest_time_of_delivery: datetime
    parcel: Parcel
    status: str
    delivery_job_id: str
```

```json
{
  "id": "O1001",
  "consumer": {
    "id": "C1001",
    "name": "John Smith",
    "phone_number": "+1234567890",
    "email": "john.smith@example.com",
    "location_id": "10001",
    "notification_ids": ["4001"]
  },
  "business_id": "00000000-0000-0000-0000-000000000001",
  "bill_id": "B1001",
  "latest_time_of_delivery": "2024-12-26T18:00:00.000Z",
  "parcel": {
    "size": "medium",
    "weight": 2.5,
    "dimensions": { "length": 15, "width": 10, "height": 8 },
    "fragile": true
  },
  "status": "pending",
  "delivery_job_id": "DJ1001"
}
```
