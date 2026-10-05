#!/usr/bin/python3
"""
Lists all states starting with N from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def main():
    """Connects to MySQL and prints states starting with N."""
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cur.fetchall():
        if row[1][0] == "N":
            print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
