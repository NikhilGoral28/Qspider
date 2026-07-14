from gensim.models import FastText


sentences = [["deep","learning","is","fun"],["machine","learning","is","powerful"]]

model = FastText(sentences=sentences,vector_size = 50,window=2,min_count=1,min_n=2)

print(model.wv["learning"])   
print("-----------------------------------")
print(model.wv.most_similar("learning"))  



#it does not gives the error
#advance of word2vec