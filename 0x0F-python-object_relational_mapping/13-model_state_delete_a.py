#!/usr/bin/python3
"""
Deleting objects
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    deleting obj
    """

    urldb = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(urldb)
    Session = sessionmaker(bind=engine)

    session = Session()

    for instance in session.query(State).filter(State.name.contains('a')):
        session.delete(instance)

    session.commit()
    session.close()
