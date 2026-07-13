from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')

lemmitizer = WordNetLemmatizer()
print(lemmitizer.lemmatize('Studies',pos='a')) #Studies

print(lemmitizer.lemmatize('better',pos='a'))  #good

print(lemmitizer.lemmatize('playing',pos='v'))  #play

print(lemmitizer.lemmatize('better'))



#by default it consider noun as POS
#it works based on the POS, it finds out the pos of the  word from lexical database (WoordNEt)
#then assign the root words froom lexical database