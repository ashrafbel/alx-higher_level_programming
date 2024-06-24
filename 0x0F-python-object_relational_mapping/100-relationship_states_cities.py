#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco" in the database.
"""
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from relationship_state import Base, State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    s_new = State(name='California')
    c_new = City(name='San Francisco')
    s_new.cities.append(c_new)
    session.add(s_new)
    session.add(c_new)
    session.commit()
