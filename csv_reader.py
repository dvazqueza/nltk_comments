import csv
import os
import sys
import codecs
import sqlite3 as lite
import nltk_comments.db_util

con = None

try:
    # con = lite.connect('C:\\Users\\dvazquez\\sandbox\\sqlite3\\comments.db')
    con = lite.connect('GGCommentsDB')
    cur = con.cursor()
    with con:
        cur = con.cursor()


        currentDir = os.path.dirname(sys.argv[0])
        grades_file= currentDir + '/Comments/GRADES/IT2A2-I1-report.csv'

        with codecs.open(grades_file, 'r', encoding='cp1252') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in spamreader:
                type = ""
                for counter, cadena in enumerate(row):
                    cadena = cadena.replace("\n"," ")
                    if counter == 0 :
                        if cadena.startswith("Scoresheet"):
                            type = "FL"
                            print ("First Line")
                        elif cadena == "":
                            type = "AS"
                            print ("Second Line")
                        else:
                            type = "ST"
                            print ("Student")
                    row[counter] = cadena


                cur.execute()
                print('|'.join(row))

except lite.Error as e:

    print("Error %s:" % e.args[0])
    sys.exit(1)

finally:

    if con:
        con.close()



