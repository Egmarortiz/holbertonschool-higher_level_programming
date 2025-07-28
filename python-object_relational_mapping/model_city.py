#!/usr/bin/python3
"""
Define a City class mapped to the MySQL 'cities' table.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    """
    ORM model for the 'cities' table:
    - id: auto-generated unique integer, non-null, primary key
    - name: string up to 128 chars, non-null
    - state_id: integer, non-null, foreign key to states.id
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
