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
        "SELECT * FROM states WHERE name ='{}'".format(sys.argv[4]))
   
    result = cursor.fetchall()
    # Process the data
    for row in result:
        print(row)
