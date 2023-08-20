#!/usr/bin/python3
"""
CHanging name
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Updating value
    """

    urlDb = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(urlDb)
    Session = sessionmaker(bind=engine)

    session = Session()

    stateValue = session.query(State).filter(State.id == '2').first()
    stateValue.name = 'New Mexico'
    session.commit()
    session.close()
