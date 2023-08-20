#!/usr/bin/python3
"""
Safe from MySql Injection
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Accessing DB
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as curserVar:
        curserVar.execute("""
            SELECT
                *
            FROM
                states
            WHERE
                name LIKE BINARY %(name)s
            ORDER BY
                states.id ASC
        """, {
            'name': argv[4]
        })

        rows = curserVar.fetchall()
