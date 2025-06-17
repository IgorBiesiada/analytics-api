from api.db.config import DATABASE_URL
from fastapi import APIRouter
from .schemas import EventSchema, EventListSchema, EventCreateSchema, EventUpdateSchema

router = APIRouter()


@router.get("/")
def read_events() -> EventListSchema:
    print(DATABASE_URL)
    return {
       "result": [
           {"id":1},
           {"id":2},
           {"id":3}
       ],
        "count": 3
    }

#send data
@router.post("/")
def create_events(payload:EventCreateSchema) -> EventSchema:
    print(payload.page)
    data = payload.model_dump()     #payload -> dict
    return {"id": 123, **data}


@router.get("/{event_id}")
def get_event(event_id:int) -> EventSchema:
    return {"id": event_id}

@router.put("/{event_id}")
def update_event(event_id:int, payload:EventUpdateSchema) -> EventSchema:
    data = payload.model_dump()
    return {"id": event_id, **data}
