#!/usr/bin/python3
"""
Script that deletes all State objects
with a name containing the letter 'a' from the database hbtn_0e_6_usa.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]
    )
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    states_to_delete = session.query(State).filter(State.name.contains('a'))
    for instance in states_to_delete:
        session.delete(instance)

    session.commit()
    session.close()
