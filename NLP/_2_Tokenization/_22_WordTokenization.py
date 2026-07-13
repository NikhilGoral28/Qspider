#Example 1
#using basic python

text = 'I love NLP!!!'

tokens = text.split()
print(tokens)

#does not remove punctuation
#not suitable for real time NLP


#example 2
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize

text = "I'm loving NLP!!"

tokens = word_tokenize(text)
print(tokens)


#example 3 using spacy

import spacy

nlp = spacy.load('en_core_web_sm')

text = "i'm loving NLP!!!"

doc = nlp(text)
tokens = [token.text for token in doc]

print(tokens)