import nltk
from nltk.corpus import treebank

def sentenceAnalysis(sentence):
    tokens = nltk.word_tokenize(sentence)

    print(tokens)
    tagged = nltk.pos_tag(tokens)
    tagged[0:6]
    print(tagged)
    entities = nltk.chunk.ne_chunk(tagged)
    print(entities)


sentence = """At eight o'clock on Thursday morning
... Arthur didn't feel very good."""
sentenceAnalysis(sentence)


comments_file= open('C:\\Users\\dvazquez\\PycharmProjects\\nltk_comments\\nltk_comments\\Comments\\SOURCE\\Form3.txt')
raw = comments_file.read()
print (type(raw))
print (len(raw))
print (raw[:75])


sentence_tokens = nltk.sent_tokenize(raw)
print (type(sentence_tokens))
print (len(sentence_tokens))

for index, sentence in enumerate(sentence_tokens):
    if (sentence.startswith('Exam Grade:')
        or sentence.startswith('Term Grade:')
        or sentence.startswith('Practical Exam Grade:')
        or sentence.startswith('Theory Exam Grade:')):
        # print (index, sentence)
        sentence_tokens.pop(index)
    else :
        print (sentence)
        sentenceAnalysis(sentence)



