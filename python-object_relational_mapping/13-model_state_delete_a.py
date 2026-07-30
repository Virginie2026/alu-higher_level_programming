#!/usr/bin/python3
"""Deletes all State objects with a name containing 'a' from database."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, binary
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State).filter(
        binary(State.name).like('%a%')
    ).delete(synchronize_session=False)

    session.commit()
    session.close()
