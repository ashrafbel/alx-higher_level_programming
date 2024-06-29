#!/usr/bin/python3
"""
Lists all City objects from the database.
"""
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    ct = session.query(State, City).join(City).order_by(City.id)
    for st, c in ct:
        print("{}: ({}) {}".format(st.name, c.id, c.name))
    session.close()
