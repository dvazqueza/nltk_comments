import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('C:\\Users\\dvazquez\\sandbox\\sqlite3\\comments.db')
    # cur = con.cursor()

    # cur.execute("SELECT * FROM Cars")

    # rows = cur.fetchall()

    # for row in rows:
    #    print (row)

    with con:
        con.row_factory = lite.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM Cars")

        col_names = [cn[0] for cn in cur.description]

        rows = cur.fetchall()

        print (
            "%s %-10s %s" % (col_names[0], col_names[1], col_names[2]))

        for row in rows:
            print ("|%s |%s |%s" % (row["Id"], row["Name"], row["Price"]))

except lite.Error as e:

    print("Error %s:" % e.args[0])
    sys.exit(1)

finally:

    if con:
        con.close()