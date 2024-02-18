#!/usr/bin/python3
''' select state module'''

import MySQLdb
import sys

if __name__ == "__main__":
    # Establish MySQL connection
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    # Create cursor object
    cursor = db.cursor()
    # Use execute method to make query
    cursor.execute(
        "SELECT DISTINCT c.id, c.name, s.name FROM states AS s "
        "INNER JOIN cities AS c "
        "ON s.id = c.state_id")

   
    result = cursor.fetchall()
    # Process the data
    for row in result:
        print(row)
