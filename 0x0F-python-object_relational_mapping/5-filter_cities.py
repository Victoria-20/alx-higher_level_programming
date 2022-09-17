#!/usr/bin/python3
""" lists all states with a name starting with N from the database """


if __name__ == "__main__":

    import MySQLdb
    import sys
    # argument variables
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    # database connection
    db = MySQLdb.connect(
                        host="localhost", port=3306, user=user,
                        passwd=password, db=database)

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities INNER \
        JOIN states ON cities.state_id = states.id \
        WHERE states.name = %s ORDER BY \
        cities.id ASC", (sys.argv[4],))

    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    # Close cursor
    cur.close()
    # close db
    db.close()
