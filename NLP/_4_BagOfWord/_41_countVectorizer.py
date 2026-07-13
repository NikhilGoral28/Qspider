from sklearn.feature_extraction.text import CountVectorizer

sentence = ['i love nlp','i love coding']

vectorizer = CountVectorizer()

x = vectorizer.fit_transform(sentence)
print(vectorizer.get_feature_names_out())
print('----')
print(x)
print('------')
print(x.toarray())