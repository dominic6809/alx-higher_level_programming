#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        )
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    new_instance = session.query(State).filter_by(id=2).first()
    if new_instance:
        new_instance.name = 'New Mexico'
        session.commit()

    session.close()
