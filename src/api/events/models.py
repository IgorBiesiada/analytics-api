from datetime import datetime, timezone
from typing import List, Optional
from sqlmodel import SQLModel, Field
import sqlmodel

def get_utc_now():
    return datetime.now(timezone.utc).replace(tzinfo=timezone.utc)


class EventCreateSchema(SQLModel):
    page: str
    description: Optional[str] = ''

class EventUpdateSchema(SQLModel):
    description: str

class EventModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    page: Optional[str] = ''
    description: Optional[str] = ''
    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlmodel.DateTime(timezone=True),
        nullable=False
)
    updated_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlmodel.DateTime(timezone=True),
        nullable=False
)

class EventListSchema(SQLModel):
    result: List[EventModel]
    count: int