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
        "SELECT c.name FROM states AS s "
        "INNER JOIN cities As c "
        "ON s.id = c.state_id "
        "WHERE s.name = {};".format(sys.argv[4]))

    result = cursor.fetchall()
    # Process the data
    # Extract city names from the result and store them in a list
    city_names = [row[0] for row in result]

    # Join the city names with commas
    city_names_str = ", ".join(city_names)
    
    # Print the concatenated city names
    print(city_names_str)
