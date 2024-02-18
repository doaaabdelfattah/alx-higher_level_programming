#!/usr/bin/python3
''' select state module'''

import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve MySQL connection parameters from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Establish MySQL connection
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    # Create cursor object
    cursor = db.cursor()

    # Execute SELECT query to retrieve states, sorted by id in ascending order
    # Use execute method to make query
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    # Fetching: retrieving data from a database after executing a SELECT query.
    # fetchall(): retrieves all rows of a query result set as a list of tuples.
    result = cursor.fetchall()
    # Process the data
    for row in result:
        print(row)
    # good practice to close the cursor to free up resources
    cursor.close()
