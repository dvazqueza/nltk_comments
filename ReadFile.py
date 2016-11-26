
def openFile(filename):

    listOfLines = []

    with open(filename, 'r') as txt:
        listOfLines = list(txt)
    txt.closed

    for line in listOfLines:
        #print(line)
        split_line(line)


def split_line(line):
    # split the text
    sentences = line.split(".")

    # for each word in the line:
    for sentence in sentences:
        sentence = sentence.lstrip()
        sentence = sentence.rstrip()
        # print the word
        if not(len(sentence) == 0 or sentence.isspace()):
            analize_line(sentence)

def analize_line(line):
    print(line)


####  MAIN PROCEDURE
openFile('Comments/SOURCE/Form3.txt')