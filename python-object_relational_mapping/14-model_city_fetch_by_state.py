#!/usr/bin/python3
"""
Print all City objects from the database hbtn_0e_14_usa
in the format: <state name>: (<city id>) <city name>.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <mysql_username> "
              "<mysql_password> <database_name>")
        sys.exit(1)

    mysql_user, mysql_pass, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL on localhost:3306
    engine = create_engine(
        f"mysql+mysqldb://{mysql_user}:{mysql_pass}@localhost:3306/{db_name}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Join City → State, order by City.id
    results = (session.query(State.name, City.id, City.name)
                     .join(City, State.id == City.state_id)
                     .order_by(City.id)
              )

    for state_name, city_id, city_name in results:
        print(f"{state_name}: ({city_id}) {city_name}")

    session.close()
