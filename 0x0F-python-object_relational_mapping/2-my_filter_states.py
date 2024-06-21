#!/usr/bin/python3
"""
script that takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    db_connect = db.connect(host="localhost", user=argv[1], port=3306,
                            passwd=argv[2], db=argv[3])
    cur_cursor = db_connect.cur_cursor()

    cur_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
                        states.id ASC".format(argv[4]))
    rows_selected = cur_cursor.fetchall()

    for row in rows_selected:
        print(row)