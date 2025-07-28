#!/usr/bin/python3
"""
Print the State object with the name passed as argument from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4 and len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} <mysql_username> <mysql_password> "
              "<database_name> [<state_name>]")
        sys.exit(1)

    mysql_user, mysql_pass, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    state_name = sys.argv[4] if len(sys.argv) == 5 else ""

    engine = create_engine(
        f"mysql+mysqldb://{mysql_user}:{mysql_pass}"
        f"@localhost:3306/{db_name}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch the first State whose name matches exactly (SQL-safe)
    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
