#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    access = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = access.cursor()
    states = argv[4]
    sql = '''
          SELECT cities.name
          FROM cities
          JOIN states ON cities.state_id = states.id
          WHERE states.name = %s
          ORDER BY cities.id ASC
          '''
    try:
        cur.execute(sql, (states, ))
        states = cur.fetchall()

        states = [i[0] for i in states]

        print(', '.join(states))
    except Exception as e:
        raise

    cur.close()
    access.close()
