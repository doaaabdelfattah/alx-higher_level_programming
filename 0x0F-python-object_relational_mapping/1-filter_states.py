#!/usr/bin/python3
''' select state module'''

import MySQLdb
import sys

if __name__ == "__main__":
    # Establish MySQL connection
    db = MySQLdb.connect(
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    # Create cursor object
    cursor = db.cursor()
    # Use execute method to make query
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%'")
    # Fetching: retrieving data from a database after executing a SELECT query.
    # fetchall(): retrieves all rows of a query result set as a list of tuples.
    result = cursor.fetchall()
    # Process the data
    for row in result:
        print(row)
    # good practice to close the cursor to free up resources
    cursor.close()
