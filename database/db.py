from typing import Optional

from sqlalchemy import create_engine, Engine, exists, select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from const_package import credentials
from database.models import Base, User

engine: Optional[Engine]


def connect_to_database():
    global engine
    engine = create_engine(credentials.DB_CONNECTION_STRING, echo=True)

    Base.metadata.create_all(engine)


def is_user_exists(tg_id):
    with Session(engine) as session:
        return session.query(exists().where(User.tg_id == tg_id)).scalar()


def get_user_by_tg_id(tg_id) -> User:
    with Session(engine) as session:
        try:
            return session.query(User).filter(User.tg_id == tg_id).one()
        except NoResultFound as e:
            print(e)


def create_user(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()


def update_user(tg_id, changes: dict):
    with Session(engine) as session:
        if is_user_exists(tg_id):
            session.query(User).filter(User.tg_id == tg_id).update(changes)
            session.commit()
