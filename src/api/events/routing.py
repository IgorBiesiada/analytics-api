from api.db.config import DATABASE_URL
from fastapi import APIRouter, Depends, HTTPException
from .models import EventModel, EventListSchema, EventCreateSchema, EventUpdateSchema
from api.db.session import get_session
from sqlmodel import Session, select

router = APIRouter()


@router.get("/", response_model=EventListSchema)
def read_events(session:Session = Depends(get_session)):
    query = select(EventModel).order_by(EventModel.id.desc()).limit(10)
    result = session.exec(query).all()
    return {
       "result": result,
        "count": len(result)
    }

#send data
@router.post("/", response_model=EventModel)
def create_events(payload:EventCreateSchema, session:Session = Depends(get_session)):
    print(payload.page)
    data = payload.model_dump()     #payload -> dict
    obj = EventModel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj

@router.get("/{event_id}", response_model=EventModel)
def get_event(event_id:int, session:Session = Depends(get_session)):
    query = select(EventModel).where(EventModel.id == event_id)
    result = session.exec(query).first()
    if not result:
        raise HTTPException(status_code=404, detail='event not found')
    return result

@router.put("/{event_id}", response_class=EventModel)
def update_event(event_id:int, payload:EventUpdateSchema, session:Session = Depends(get_session)):
    query = select(EventModel).where(EventModel.id == event_id)
    obj = session.exec(query).first()
    if not obj:
        raise HTTPException(status_code=404, detail='event not found')
    
    data = payload.model_dump()
    for key, value in data.items():
        setattr(obj, key, value)
    
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj
    
@router.delete("/{event_id}", response_class=EventModel)
def delete_event(event_id:int, session: Session = Depends(get_session)):
    event = session.get(EventModel, event_id)
    if not event:
        raise HTTPException(status_code=404, detail='event not found')
    session.delete(event)
    session.commit()
    return {"ok": True}