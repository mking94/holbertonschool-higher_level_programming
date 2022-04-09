#!/usr/bin/python
"""
script that lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb
if __name__ == "__main__":
    db_connection = MySQLdb.connect(
        host='127.0.0.1',
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],

    )
    cursor = db_connection.cursor()
    cursor.execute("SELECT * from `states` ORDER BY id;")
    liste = cursor.fetchall()
    print(*liste, sep="\n")
    cursor.close()
    db_connection.close()
