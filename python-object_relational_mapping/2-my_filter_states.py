#!/usr/bin/python3
"""Displays all values in the states table where name matches the argument."""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_searched = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"
    cursor.execute(query.format(state_searched))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
