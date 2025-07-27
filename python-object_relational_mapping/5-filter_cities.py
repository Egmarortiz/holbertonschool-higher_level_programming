#!/usr/bin/python3
"""
Lists all cities of a given state (safe from MySQL injection).
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Grab credentials and state name from argv
    mysql_user, mysql_pass, db_name, state_name = (
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        sys.argv[4]
    )

    # Connect to MySQL on localhost:3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_pass,
        db=db_name
    )
    cursor = db.cursor()

    # One parameterized query to fetch city names in the given state
    query = (
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )
    cursor.execute(query, (state_name,))

    # Fetch and print as comma-separated list
    rows = cursor.fetchall()
    print(", ".join(row[0] for row in rows))

    cursor.close()
    db.close()
