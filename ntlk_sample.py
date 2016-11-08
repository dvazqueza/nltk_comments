import nltk
from nltk.corpus import treebank

sentence = """At eight o'clock on Thursday morning
... Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)

print (tokens)

tagged = nltk.pos_tag(tokens)
tagged[0:6]

print (tagged)

entities = nltk.chunk.ne_chunk(tagged)
print (entities)

t= treebank.parsed_sents('C:\\Users\\dvazquez\\Google Drive\\PycharmProjects\\GGComments\\news.txt')[0]
t.draw()