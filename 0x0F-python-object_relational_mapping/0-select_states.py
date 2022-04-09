#!/usr/bin/python
import sys
import MySQLdb
if __name__ == "__main__":
    try:
        db_connection = MySQLdb.connect(
            host='127.0.0.1',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
        cursor = db_connection.cursor()
        cursor.execute("SELECT * from `states`;")
        liste = cursor.fetchall()
        print(*liste, sep="\n")
        db_connection.close()
    except Exception as e:
        print(e)
