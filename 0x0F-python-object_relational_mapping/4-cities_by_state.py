#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    access = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = access.cursor()
    sql = ''' SELECT cities.id,cities.name, states.name
          FROM cities
          JOIN states ON cities.state_id = states.id
          ORDER BY id ASC
          '''
    try:
        cur.execute(sql)
        cities = cur.fetchall()

        for city in cities:
            print(city)
    except Exception as e:
        raise

    cur.close()
    access.close()
