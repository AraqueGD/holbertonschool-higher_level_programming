#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    access = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = access.cursor()
    name_db = argv[4]
    sql = "SELECT * FROM states WHERE name = %s \
          COLLATE latin1_general_cs ORDER BY id ASC"
    try:
        cur.execute(sql, (name_db, ))
        states = cur.fetchall()

        for state in states:
            print(state)
    except Exception as e:
        raise

    cur.close()
    access.close()
