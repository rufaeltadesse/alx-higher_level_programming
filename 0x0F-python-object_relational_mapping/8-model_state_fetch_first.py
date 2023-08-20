#!/usr/bin/python3
"""
First state print.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Accessing DB
    """

    ulrdb = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(ulrdb)
    Session = sessionmaker(bind=engine)

    session = Session()
    insVar = session.query(State).order_by(State.id).first()

    if insVar is None:
        print('Nothing')
    else:
        print('{0}: {1}'.format(insVar.id, insVar.name))
