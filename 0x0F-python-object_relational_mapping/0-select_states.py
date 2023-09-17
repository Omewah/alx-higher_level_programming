#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY states.id ASC;")
    rows = c.fetchall()

    for row in rows:
        print(row)
