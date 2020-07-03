#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities of that state
"""
import sys
import os
import MySQLdb

if __name__ == '__main__':
    count = 0
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN\
    states ON cities.state_id=states.id WHERE states.name='{}'\
    ORDER BY cities.id ASC".format(sys.argv[4],))
    query_rows = cur.fetchall()
    len_query = len(query_rows)
    for value in query_rows:
        count += 1
        if count < len_query:
            print('{}, '.format(value[0],), end="")
        else:
            print('{}'.format(value[0],))
    cur.close()
    conn.close()
