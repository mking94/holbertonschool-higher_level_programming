#!/usr/bin/python
import sys
import MySQLdb
if __name__ == "__nanme__":
    db_connection= MySQLdb.connect("127.0.0.1",sys.arv[1],sys.arv[2],sys.arv[3])
