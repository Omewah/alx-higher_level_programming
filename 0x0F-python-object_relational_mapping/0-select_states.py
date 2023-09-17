#!/usr/bin/python3
# a script that lists all the states in a database

import sys
import MySQLdb

if __name__ == "__main__":
    dbase =
    MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], dbase=sys.argv[3])
    a = dbase.cursor()
    a.execute("SELECT * FROM `states`")
    [print(state) for state in a.fetchall()]
