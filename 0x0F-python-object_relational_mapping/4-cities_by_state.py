#!/usr/bin/python3
"""
it lists all cities from
the database `hbtn_0e_4_usa`.
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """
    Access the database and get the cities from the db
    """

    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    with db_connect.cursor() as db_cursor:
        cursor.execute("SELECT cities.id, cities.name, states.name \
                                FROM cities JOIN states ON cities.state_id \
                                = states.id ORDER BY cities.id ASC")
        rows_selected = cursor.fetchall()

    if rows_selected is not None:
        for row in rows_selected:
            print(row)
