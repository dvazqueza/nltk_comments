import sqlite3 as lite
import sys

con = None

try:
    # con = lite.connect('C:\\Users\\dvazquez\\sandbox\\sqlite3\\comments.db')
    con = lite.connect('GGCommentsDB.db')
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')

    data = cur.fetchone()

    print ("SQLite version: %s" % data)

    with con:
        cur = con.cursor()
        # cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
        cur.execute("INSERT INTO Comments VALUES(1,'Comentario ejemplo 1','')")
        cur.execute("INSERT INTO Comments VALUES(2,'Comentario ejemplo 2','')")
        cur.execute("INSERT INTO Comments VALUES(3,'Comentario ejemplo 3','')")
        cur.execute("INSERT INTO Comments VALUES(4,'Comentario ejemplo 4','')")
        cur.execute("INSERT INTO Comments VALUES(5,'Comentario ejemplo 5','')")
        cur.execute("INSERT INTO Comments VALUES(6,'Comentario ejemplo 6','')")

except lite.Error as e:

    print("Error %s:" % e.args[0])
    sys.exit(1)

finally:

    if con:
        con.close()