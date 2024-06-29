#!/usr/bin/python3
"""
Class definition of a City
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class City(Base):
    """
    City class that inherits from Base
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    stid = Column(Integer, ForeignKey('states.id'), nullable=False)
