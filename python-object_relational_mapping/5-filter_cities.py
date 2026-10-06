#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def main():
    """Connects to MySQL and prints cities of a given state."""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()
    cur.execute(
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (state_name,)
    )

    rows = cur.fetchall()
    cities = [row[0] for row in rows]
    print(", ".join(cities))

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
