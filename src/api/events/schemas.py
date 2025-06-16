from typing import List, Optional
from pydantic import BaseModel

class EventCreateSchema(BaseModel):
    page: str
    description: Optional[str] = ''

class EventUpdateSchema(BaseModel):
    description: str

class EventSchema(BaseModel):
    id: int
    page: Optional[str] = ''
    description: Optional[str] = ''

class EventListSchema(BaseModel):
    result: List[EventSchema]
    count: int
    