#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    mysql_user, mysql_pass, db_name = sys.argv[1:4]

    engine = create_engine(f"mysql+mysqldb://{mysql_user}:{mysql_pass}@localhost:3306/{db_name}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects, ordered by id
    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")

    session.close()
