#!/usr/bin/python3
"This scropt for lists staes"

from sys import argv
import MySQLdb

if __name__ == "__main__":
    d_b = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3], charset="utf8")
cur = d_b.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
q_r = cur.fetchall()
for r in q_r:
    print(r)
cur.close()
d_b.close()
