#!/usr/bin/python3
"""
Script to return the first State object from the database hbtn_0e_6_usa.
Username, password, and database name are provided as arguments.
"""
from sqlalchemy import create_engine
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    s = session.query(State).order_by(State.id).first()
    if s is None:
        print("Nothing")
    else:
        print("{}: {}".format(s.id, s.name))
    session.close()
