#!/usr/bin/python3
""" lists all states from the database """

import sys
import MySQLdb


if __name__ == "__main__":
    if (len(sys.argv) == 4):
        user = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user,
            passwd=password,
            db=database,
            charset="utf8")

        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")

        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)

        # Close all cursors
        cur.close()
        # Close db connection
        db.close()
