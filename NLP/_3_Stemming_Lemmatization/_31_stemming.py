#Example one

#porter stemming


from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

words = ['playing','studies','happiness']    #play,studi,happi

for word in words:
    print(stemmer.stem(word))


#does not understand the meaning of the words
#not converts the properly just removes the prefix and sufix


#Example 2

#snowball

from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer()

words = ['playing','studies','happiness']    #play,studi,happi

for w in words:
    print(stemmer.stem(w))

#it is advance version of the porter stemming, internally it uses the more rules than the porter stemmer but result gets same

#Example 3

#Lancaster stemming

from nltk.stem import LancasterStemmer
stemmer = LancasterStemmer()

words = ['playing','studies','happiness']    

for w in words:
    print(stemmer.stem(w))

#it too harsh for the word, it removes the prefix and sufix agrresively