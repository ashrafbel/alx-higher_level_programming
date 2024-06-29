#!/usr/bin/python3
"""
Script to delete all State objects with names containing
the letter 'a' from the database using SQLAlchemy.
"""

from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    delstat = session.query(State).filter(State.name.like('%a%')).all()
    for d in delstat:
        session.delete(d)
    session.commit()
    session.close()
