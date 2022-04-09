#!/usr/bin/python3
"""
Python class which allows you to connect to database and select data
"""


import MySQLdb
import sys


def filter_states():
    """"
    lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
    """
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db_cnx = MySQLdb.connect(host="localhost", port=3306, user=user,passwd=password, db=database)

    cursor = db_cnx.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    liste = cursor.fetchall()
    for row in liste:
        print(row)
    cur.close()
    db_cnx.close()


if __name__ == "__main__":
    filter_states()
