#!/usr/bin/python3
"""
Script to print the State object with the specified name from the database
using SQLAlchemy.
"""

from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    # create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    st = session.query(State).filter(State.name == argv[4]).first()
    if st:
        print("{}".format(st.id))
    else:
        print("Not found")
    session.close()
