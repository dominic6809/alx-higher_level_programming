#!/usr/bin/python3
"""
Module that adds the State object
`Louisiana` to the database `hbtn_0e_6_usa`.
"""

from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    """
    Access the database and add a state to the db.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]
    )

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    n_state = State(name="Louisiana")
    session.add(n_state)
    session.commit()

    print('{0}'.format(n_state.id))
    session.close()
