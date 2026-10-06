#!/usr/bin/python3
"""
This script lists all State objects from the database hbtn_0e_6_usa.
"""

import sys
import SQLAlchemy

def main():
    """Connects to MySQL and prints all State objects."""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()

if __name__ == "__main__":
    main()
