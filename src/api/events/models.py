from typing import List, Optional
from pydantic import BaseModel
from sqlmodel import SQLModel, Field

class EventCreateSchema(SQLModel):
    page: str
    description: Optional[str] = ''

class EventUpdateSchema(SQLModel):
    description: str

class EventSchema(SQLModel):
    #id: int | None = Field(default=None, primary_key=True)
    id: int
    page: Optional[str] = ''
    description: Optional[str] = ''

class EventListSchema(SQLModel):
    result: List[EventSchema]
    count: int