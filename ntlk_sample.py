import os
import sys
import nltk_comments.nltk_utilities as nltkUtil

# sentence = """At eight o'clock on Thursday morning
# ... Arthur didn't feel very good."""
# nltkUtil.sentenceAnalysis(sentence)

currentDir = os.path.dirname(sys.argv[0])
comments_file= open(currentDir + '/Comments/SOURCE/Form3.txt')
sentence_tokens = nltkUtil.tokenizeFile(comments_file)

# print (type(sentence_tokens))
# print (len(sentence_tokens))

for index, sentence in enumerate(sentence_tokens):
    if (sentence.startswith('Exam Grade:')
        or sentence.startswith('Term Grade:')
        or sentence.startswith('Practical Exam Grade:')
        or sentence.startswith('Theory Exam Grade:')):
        # print (index, sentence)
        sentence_tokens.pop(index)
    else :
        print (sentence)
        nltkUtil.sentenceAnalysis(sentence)
