#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """


if __name__ == "__main__":
    import MySQLdb
    import sys
    db_cnx = MySQLdb.connect(
        host="localhost", user=sys.argv[1],
        password=sys.argv[2], database=sys.argv[3],
        charset="utf8")
    cursor = db_cnx.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    liste = cursor.fetchall()
    for row in liste:
        print(row)
    cursor.close()
    db_cnx.close()
