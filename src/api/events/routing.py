from fastapi import APIRouter
from .schemas import EventSchema, EventListSchema

router = APIRouter()


@router.get("/")
def read_events() -> EventListSchema:
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
def send_events() -> EventListSchema:
    return {
       "result": [
           {"id":1},
           {"id":2},
           {"id":3}
       ],
        "count": 3
    }


@router.get("/{event_id}")
def get_event(event_id:int) -> EventSchema:
    return {"id": event_id}
