#!/usr/bin/python3
""" takes in the name of a state as an argument and lists all cities"""
import MySQLdb
from sys import argv


if __name__ == '__main__':

    d_b = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3])

    cur = d_b.cursor()
    q = """SELECT cities.id, cities.name, states.name
           FROM cities
           INNER JOIN states ON cities.state_id=states.id
           WHERE states.name = %s
           ORDER BY cities.id ASC"""
    cur.execute(q, (argv[4],))
    r = cur.fetchall()
    for x in r:
        print(x)
    cur.close()
    d_b.close()
