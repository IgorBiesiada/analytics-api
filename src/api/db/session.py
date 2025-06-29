import sqlmodel
from .config import DATABASE_URL
from sqlmodel import SQLModel

if DATABASE_URL == "":
    raise NotImplementedError("DATABASE_URL need to be set")

engine = sqlmodel.create_engine(DATABASE_URL)


def init_db():
    print('creating db')
    SQLModel.metadata.create_all(engine)