#!/usr/bin/python3
"""
Listing all cities
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Accessing database
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as curserVar:
        curserVar.execute("""
            SELECT
                cities.id, cities.name, states.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            ORDER BY
                cities.id ASC
        """)

        rows = curserVar.fetchall()

    if rows is not None:
        for row in rows:
            print(row)

    if rows is not None:
        for row in rows:
            print(row)
