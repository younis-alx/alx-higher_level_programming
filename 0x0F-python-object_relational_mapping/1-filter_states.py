#!/usr/bin/python3
"""lists all states with a name starting with N (upper N)"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute(
        """SELECT * FROM states WHERE name RLIKE '^N' 
        ORDER BY states.id ASC""")
    [print(tup) for tup in cur.fetchall()]
    cur.close()
