#example 1

from nltk.tokenize import sent_tokenize

text = "Dr.Smith loves NLP. He works at Google"
sentences = sent_tokenize(text)

print(sentences)


#Example 2

import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp(text)
sentences = [sent.text for sent in doc.sents]

print(sentences)