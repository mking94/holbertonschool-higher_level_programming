#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities JOIN states\
                ON states.id = cities.state_id\
                Where states.name = %s\
                ORDER BY cities.id ASC", (sys.argv[4], ))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    db.close()