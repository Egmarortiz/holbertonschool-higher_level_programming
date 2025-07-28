#!/usr/bin/python3
"""
Changes the name of the State object with id = 2 to New Mexico in the database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    mysql_user, mysql_pass, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL on localhost:3306
    engine = create_engine(f"mysql+mysqldb://{mysql_user}:{mysql_pass}@localhost:3306/{db_name}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch the State with id == 2
    state = session.query(State).filter(State.id == 2).first()
    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()
