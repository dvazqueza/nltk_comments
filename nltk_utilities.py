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

def tokenizeFile(file):
    raw = file.read()
    print(type(raw))
    print(len(raw))
    print(raw[:75])
    sentences = nltk.sent_tokenize(raw)
    return sentences