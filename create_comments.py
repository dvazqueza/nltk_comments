import sqlite3 as lite
import sys


def CreateReports(form):

    # Keyboard Shortcut: Ctrl+q

    strComment = ""
    strTarget = ""
    strFirstName = ""
    strGender = ""

    strHeSheCaps = ""
    strHeSheNoCaps = ""
    strHisHerCaps = ""
    strHisHerNoCaps = ""
    strHimHerNoCaps = ""

    nFirstNameCol = ""
    nGenderCol = ""
    nMaxRecords = ""



    # get tokens..

    strTokens = []
    strTokenFemale = []
    strTokenMale = []

    try:
        con = None
        con = lite.connect('GGCommentsDB.db')
        cur = con.cursor()
        cur.execute('SELECT SQLITE_VERSION()')

        # Do this instead

        nRow = 0

        for row in cur.execute('SELECT * FROM Tokens'):

            strTokens.append(row[1])
            strTokenMale.append(row[2])
            strTokenFemale.append(row[3])
            nRow += 1

        for student in cur.execute('SELECT * FROM Students WHERE form= ?', form):
            intStudentId = student[0]
            strFirstName = student [2]
            strGender = student[4]

    except lite.Error as e:

        print("Error %s:" % e.args[0])
        sys.exit(1)

    finally:

        if con:
            con.close()

    print(strTokens)
    print(strTokenMale)
    print(strTokenFemale)

    #  get each comment and replace tokens..

'''
'REPLACE COMMENT..

For
col = 5
To
11

strComment = Worksheets("Create").Cells(nRow, col)

If(strComment <> "")
And(col <> 10)
Then
For
i = 0
To
15
'hack! try 15 times to replace key word tags..
For
j = 0
To
9
strComment = Replace(strComment, "<firstname>", strFirstName)
If(strGender="M")
Then
strComment = Replace(strComment, strTokens(j + 1), strTokenMale(j + 1))
End
If
If(strGender="F")
Then
strComment = Replace(strComment, strTokens(j + 1), strTokenFemale(j + 1))
End
If
Next
j
Next
i

Worksheets("Create").Cells(nRow, col) = strComment
End
If

Next
col

'REPLACE TARGET
For
col = 11
To
16
strTarget = Worksheets("Create").Cells(nRow, col)

If(strTarget <> "")
And(col <> 14)
Then
For
i = 0
To
15
'hack! try 15 times to replace key word tags..
For
j = 0
To
9
strTarget = Replace(strTarget, "<firstname>", strFirstName)
If(strGender="M")
Then
strTarget = Replace(strTarget, strTokens(j + 1), strTokenMale(j + 1))
End
If
If(strGender="F")
Then
strTarget = Replace(strTarget, strTokens(j + 1), strTokenFemale(j + 1))
End
If
Next
j
Next
i
End
If

Worksheets("Create").Cells(nRow, col) = strTarget
Next
col
Next
nRow

'''

CreateReports()