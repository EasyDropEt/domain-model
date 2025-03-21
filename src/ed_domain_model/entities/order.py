from datetime import datetime
from enum import StrEnum
from typing import NotRequired, TypedDict
from uuid import UUID


class OrderStatus(StrEnum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    FAILED = "failed"


class ParcelSize(StrEnum):
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
    id: UUID
    consumer_id: UUID
    business_id: UUID
    bill_id: UUID
    latest_time_of_delivery: datetime
    parcel: Parcel
    order_status: OrderStatus
    delivery_job_id: NotRequired[UUID]
