#!/usr/bin/python3
"""
Script to update the name of a State object in the database
using the SQLAlchemy module.
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
    upsate = session.query(State).filter_by(id='2').first()
    upsate.name = "New Mexico"
    session.commit()
    session.close()
