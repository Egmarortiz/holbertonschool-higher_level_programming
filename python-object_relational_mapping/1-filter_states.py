#!/usr/bin/python3
"""
List all states with a name starting with N (upper N).
"""


import sys
import MySQLdb


if __name__ == "__main__":
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create
    cursor = db.cursor()

    # Execute SQL query to select states starting with 'N' ordered by id
    cursor.execute(
            "SELECT * FROM states "
            "WHERE name LIKE BINARY 'N%' "
            "ORDER BY id ASC"
        )

    # Fetch all results
    results = cursor.fetchall()

    # Print results
    for row in results:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
