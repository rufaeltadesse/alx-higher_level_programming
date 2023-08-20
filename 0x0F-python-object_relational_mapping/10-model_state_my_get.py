#!/usr/bin/python3
"""
Printing state object id
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Accessing DB
    """

    urldb = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(urldb)
    Session = sessionmaker(bind=engine)

    session = Session()
    myInsVar = session.query(State).filter(State.name == argv[4]).first()

    if myInsVar is None:
        print('Not found')
    else:
        print('{0}'.format(myInsVar.id))
