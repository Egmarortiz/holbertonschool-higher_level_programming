#!/usr/bin/python3
"""
Lists all states
"""

import sys
import MySQLdb


def main():
    # Grab credentials and database name from command-line arguments
    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL on localhost:3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )
    cursor = db.cursor()

    # Execute the query, ordering by states.id ascending
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print each row as a tuple
    for row in cursor.fetchall():
        print(row)

    # Clean up
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
