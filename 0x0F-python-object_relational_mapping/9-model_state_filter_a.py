#!/usr/bin/python3
"""
Script that lists all State objects containing the letter 'a' in the database.
Utilizes the SQLAlchemy module.
"""
from sys import argv
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states_with_a = session.query(State).filter(State.name.like('%a%'))\
                                        .order_by(State.id).all()
    for s in states_with_a:
        print("{}: {}".format(s.id, s.name))
    session.close()
