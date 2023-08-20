#!/usr/bin/python3
"""
Listing all cities
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    accessing db
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as curserVar:
        curserVar.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': argv[4]
        })

        rows = curserVar.fetchall()

    if rows is not None:
        print(", ".join([row[1] for row in rows]))