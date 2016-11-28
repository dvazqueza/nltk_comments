import csv
import os
import sys
import codecs
import sqlite3 as lite

con = None
AllStudents = []
AllAssignments = []


try:
    # con = lite.connect('C:\\Users\\dvazquez\\sandbox\\sqlite3\\comments.db')
    con = lite.connect('GGCommentsDB.db')

    with con:
        cur = con.cursor()

        AllStudents = cur.execute("SELECT * FROM Students").fetchall()

        # print(AllStudents)

        currentDir = os.path.dirname(sys.argv[0])
        grades_file= currentDir + '/Comments/GRADES/IT2A2-I1-report.csv'

        with codecs.open(grades_file, 'r', encoding='cp1252') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            count = 1
            for row in spamreader:
                type = ""
                if row[0].startswith("Scoresheet"):
                    type = "FL"
                    print("FL: " + row[0])
                elif row[0] == "":
                    type = "AS"
                    print("AS")
                    AllAssignments = row
                    print(AllAssignments)
                    print(len(AllAssignments))
                    # for counter, assignment in enumerate(AllAssignments):
                    #    cur.execute("INSERT INTO Assignments (id, class, title) VALUES (?,?,?)",(counter,"IT2A2",assignment))
                else:
                    type = "ST"
                    print("ST:" + row[0])
                    studentName = row[0].split(",")
                    studentName[0] = studentName[0].strip()
                    studentName[1] = studentName[1].strip()
                    for student in AllStudents:
                        if student[3] == studentName[0] and student[2] == studentName[1]:
                            studentId = student[0]
                            print(str(student[0]) + ":" + student[2] + ":" + student[3])

                    for idx in range(1, len(AllAssignments)):
                        print((count, studentId, idx, row[idx]))
                        cur.execute("INSERT INTO assigment_grade (id, student_id, grade_id, grade) VALUES (?,?,?,?)",
                                    (count, studentId, idx, row[idx]))
                        count += 1
                    print(studentName)

                '''
                for counter, cadena in enumerate(row):
                    cadena = cadena.replace("\n"," ")
                    row[counter] = cadena
                    if counter == 0 :
                        if cadena.startswith("Scoresheet"):
                            type = "FL"
                        elif cadena == "":
                            type = "AS"
                        else:
                            type = "ST"

                '''

                # cur.execute()
                print('|'.join(row))

except lite.Error as e:

    print("Error %s:" % e.args[0])
    sys.exit(1)

finally:

    if con:
        con.close()



