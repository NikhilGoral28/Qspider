#Example 1

import nltk

#nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "This is a simple NLP example"

words = word_tokenize(text)

filtered = [w for w in words if w.lower() not in stopwords.words('english')]

print(filtered)


#slower ds
#need manual toeknization
#static stopwords list


#Example 2

import spacy

nlp = spacy.load("en_core_web_sm")
text = "This is a simple NLP Example"

doc = nlp(text)
filtered = [token.text for token in doc if not token.is_stop]
print(filtered)
