import csv
import os
import sys
import codecs
import sqlite3 as lite

con = None
print("Hello")
try:
    # con = lite.connect('C:\\Users\\dvazquez\\sandbox\\sqlite3\\comments.db')
    con = lite.connect('../GGCommentsDB.db')
    cur = con.cursor()

    currentDir = os.path.dirname(sys.argv[0])
    grades_file = currentDir + '/Comments/SOURCE/Comments_Column.csv'

    with codecs.open(grades_file, 'r', encoding='cp1252') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        counter = 1
        for row in spamreader:
            intId = counter
            strComment = row[0]
            strType = row[1]
            print((intId, strComment, strType))
            cur.execute('INSERT INTO Comments (id, comentario, type) VALUES (?,?,?)', (intId, strComment, strType))
            counter += 1

    con.commit()
except lite.Error as e:

    print("Error %s:" % e.args[0])
    sys.exit(1)

finally:

    if con:
        con.close()
