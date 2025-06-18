from typing import List, Optional
from pydantic import BaseModel
from sqlmodel import SQLModel, Field

class EventCreateSchema(SQLModel):
    page: str
    description: Optional[str] = ''

class EventUpdateSchema(SQLModel):
    description: str

class EventModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    page: Optional[str] = ''
    description: Optional[str] = ''

class EventListSchema(SQLModel):
    result: List[EventModel]
    count: int