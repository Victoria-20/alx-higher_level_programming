#!/usr/bin/python3
""" lists all states with a name starting with N from the database """

import sys
import MySQLdb


if __name__ == "__main__":
    if (len(sys.argv) == 5):
        user = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        searched = sys.argv[4]

        # Connect to database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user,
            passwd=password,
            db=database,
            charset="utf8")

        cur = db.cursor()
        # Execute the SQL query
        cur.execute("SELECT * FROM states WHERE name = '{}'".format(searched))

        query_rows = cur.fetchall()
        for row in query_rows:
            if row[1] == searched:
                print(row)

        # Close all cursors
        cur.close()
        # Close db connection
        db.close()
