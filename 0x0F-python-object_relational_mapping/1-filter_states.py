#!/usr/bin/python3
""" this script for lists all states start with N"""
import MySQLdb
from sys import argv


if __name__ == '__main__':

    d_b = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3])
    cur = d_b.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    r = cur.fetchall()
    for x in r:
        print(x)
    cur.close()
    d_b.close()
