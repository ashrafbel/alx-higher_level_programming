#!/usr/bin/python3
"""
Script to add the State object "Louisiana" to the database hbtn_0e_6_usa
using SQLAlchemy.
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    nstat = State(name="Louisiana")
    session.add(nstat)
    session.commit()
    print(nstat.id)
    session.close()
