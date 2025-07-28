#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa and prints its new id.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Usage: ./11-model_state_insert.py <mysql_username> <mysql_password> <database_name>
    mysql_user, mysql_pass, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL on localhost:3306
    engine = create_engine(
        f"mysql+mysqldb://{mysql_user}:{mysql_pass}@localhost:3306/{db_name}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create and add the new State
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the newly assigned id
    print(new_state.id)

    session.close()
