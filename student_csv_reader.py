import csv
import os
import sys
import codecs
import sqlite3 as lite

con = None
print ("Hello")
try:
    # con = lite.connect('C:\\Users\\dvazquez\\sandbox\\sqlite3\\comments.db')
    con = lite.connect('GGCommentsDB.db')
    cur = con.cursor()

    currentDir = os.path.dirname(sys.argv[0])
    grades_file= currentDir + '/Comments/SOURCE/DV-StudentRoster.csv'

    with codecs.open(grades_file, 'r', encoding='cp1252') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        counter = 1
        for row in spamreader:
            intId = counter
            strForm = row[0]
            strFirstName = row[1]
            strLastName = row[2]
            strGender = row[3]
            cur.execute('INSERT INTO Students (id, form, firstname, surname, gender) VALUES (?,?,?,?,?)', (intId, strForm, strFirstName,strLastName, strGender))
            counter += 1

    con.commit()
except lite.Error as e:

    print("Error %s:" % e.args[0])
    sys.exit(1)

finally:

    if con:
        con.close()



