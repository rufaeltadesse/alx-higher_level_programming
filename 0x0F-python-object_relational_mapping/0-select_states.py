#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ Accessing DB
    """
    myDb = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                           passwd=argv[2], db=argv[3])

    cursorVal = myDb.cursor()
    cursorVal.execute("SELECT * FROM states")
    rows = cursorVal.fetchall()

    for row in rows:
        print(row)
