#!/usr/bin/python3
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
        database=sys.argv[3]
    )
    cursor = db_connection.cursor()
    cursor.execute("SELECT * from states;")
    liste = cursor.fetchall()
    for row in liste:
        print(row)
    cursor.close()
    db_connection.close()
