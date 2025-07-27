#!/usr/bin/python3
import sys
import MySQLdb

def main():
    # Grab MySQL credentials and database name from the command line
    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the MySQL server on localhost:3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )
    cursor = db.cursor()

    # Select only states whose name starts with an uppercase 'N', ordered by id
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    # Print each row as a tuple
    for state in cursor.fetchall():
        print(state)

    # Clean up
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
