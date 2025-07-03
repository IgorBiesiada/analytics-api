from datetime import datetime, timezone
from typing import List, Optional
from sqlmodel import SQLModel, Field
import sqlmodel
from timescaledb import TimescaleModel
from timescaledb.utils import get_utc_now

# using get_utc_now function from timescaledb.utils
#def get_utc_now():
#    return datetime.now(timezone.utc).replace(tzinfo=timezone.utc)


class EventCreateSchema(SQLModel):
    page: str
    description: Optional[str] = ''

class EventUpdateSchema(SQLModel):
    description: str

#tracking page visits at any given time

class EventModel(TimescaleModel, table=True):
    #id: int | None = Field(default=None, primary_key=True)
    page: str = Field(index=True) #/about or /contact page 
    description: Optional[str] = ''
    #created_at: datetime = Field(
    #    default_factory=get_utc_now,
    #    sa_type=sqlmodel.DateTime(timezone=True),
    #    nullable=False
    #)
    updated_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlmodel.DateTime(timezone=True),
        nullable=False
)
    __chunk_time_interval__= "INTERVAL 1 day"
    __drop_after__ = "INTERVAL 3 months"

class EventListSchema(SQLModel):
    result: List[EventModel]
    count: int