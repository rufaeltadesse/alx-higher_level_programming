#!/usr/bin/python3
"""
Listing all object
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Accessing db
    """

    urldb = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(urldb)
    Session = sessionmaker(bind=engine)

    session = Session()

    for insVar in session.query(State).filter(State.name.contains('a')):
        print('{0}: {1}'.format(insVar.id, insVar.name))
