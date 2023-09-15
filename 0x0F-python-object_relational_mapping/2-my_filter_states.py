#!/usr/bin/python3
"""
takes in an argument and displays all values in the states\
table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states
                WHERE name LIKE BINARY '{}'
                ORDER BY states.id ASC""".format(argv[4]).strip("'"))
    [print(tup) for tup in cur.fetchall()]
    cur.close()
