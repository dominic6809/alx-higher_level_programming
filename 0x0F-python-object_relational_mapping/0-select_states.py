#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    connect to database
    """
    db_connect = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    cursor = db_connect.cursor()

    cursor.execute("SELECT * FROM states")

    rows_selected = cursor.fetchall()

    for row in rows_selected:
        print(row)
