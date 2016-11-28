import sqlite3 as lite
import sys
import random


def commentsType(comments, type):
    commentsTypeList = []
    for comment in comments:
        if comment[2] == type:
            commentsTypeList.append(comment)

    return commentsTypeList


def selectComment(commentsTypeList, grade, pct):
    strComment = ""

    commentGrade = 0

    gradeValue = (float(pct.strip('%')))
    tries = 10
    while not commentGrade > gradeValue and tries != 0:
        comment = random.choice(commentsTypeList)
        commentGrade = comment[3]
        if commentGrade > gradeValue:
            strComment = comment[1]
        else:
            tries -= 1

    return strComment


def replaceTokens(comm, tokens, firstName, gender, form):
    comm = comm.replace('<firstname>', firstName)
    for token in tokens:
        replaceValue = ''
        if gender == 'M':
            replaceValue = token[2]
        elif gender == 'F':
            replaceValue = token[3]

        if token[1] == '<subject>':
            if form == 'U6' or form == 'L6':
                replaceValue = 'Computer Science'
        comm = comm.replace(token[1], replaceValue)
    return comm


def StudentReport(student, tokens, comments):
    strTokens = []
    strTokenFemale = []
    strTokenMale = []

    nRow = 0
    for row in tokens:
        strTokens.append(row[1])
        strTokenMale.append(row[2])
        strTokenFemale.append(row[3])
        nRow += 1

    studentGrade = student[4]
    studentPct = student[5]
    intStudentId = student[0]
    strFirstName = student[1]
    strGender = student[3]
    strForm = student[6]

    finalComment = []
    finalComment.append(selectComment(commentsType(comments, 'Comment 1'), student[4], student[5]))
    finalComment.append(selectComment(commentsType(comments, 'Comment 2'), student[4], student[5]))
    finalComment.append(selectComment(commentsType(comments, 'Comment 3'), student[4], student[5]))
    finalComment.append(selectComment(commentsType(comments, 'Comment 4'), student[4], student[5]))
    finalComment.append(selectComment(commentsType(comments, 'Comment 5'), student[4], student[5]))
    finalComment.append(selectComment(commentsType(comments, 'Target 1'), student[4], student[5]))
    finalComment.append(selectComment(commentsType(comments, 'Target 2'), student[4], student[5]))
    finalComment.append(selectComment(commentsType(comments, 'Target 3'), student[4], student[5]))

    for index, comm in enumerate(finalComment):
        finalComment[index] = replaceTokens(comm, tokens, strFirstName, strGender, strForm)

    comment = ' '.join(finalComment)

    return (intStudentId, comment)

def CreateReports(form):
    con = None

    try:

        con = lite.connect('GGCommentsDB.db')
        cur = con.cursor()

        version = cur.execute('SELECT SQLITE_VERSION()').fetchall()
        print(version)

        comments = cur.execute('SELECT id,comentario,type,weight FROM Comments').fetchall()
        print(comments)

        tokens = cur.execute('SELECT id, token, male, female FROM Tokens').fetchall()
        print(tokens)

        students = cur.execute(
            "SELECT Students.id AS id, firstname, surname, gender, grade, pct, form  FROM Students,final_grade "
            "WHERE Students.id = final_grade.student_id AND form=?", ('F2',)).fetchall()
        print(students)

        count = 0
        for student in students:
            storeComment = StudentReport(student, tokens, comments)
            print(storeComment)
            cur.execute('INSERT INTO Results (id, student_id, term, final_comment) VALUES (?,?,?,?)',
                        (count, storeComment[0], 'G1', storeComment[1]))
            count += 1
        con.commit()
    except lite.Error as e:

        print("Error %s:" % e.args[0])
        sys.exit(1)

    finally:

        if con:
            con.close()


CreateReports("F2")
