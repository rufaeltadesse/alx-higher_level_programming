#!/usr/bin/python3
"""
Fetching Information
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Accessing DB
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    curserVar = db.cursor()
    curserVar.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY '{}' \
                 ORDER BY states.id ASC".format(argv[4]))
    rows = curserVar.fetchall()

    for row in rows:
        print(row)
