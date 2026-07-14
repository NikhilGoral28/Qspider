from gensim.models import Word2Vec

sentences = [["deep","learning","is","fun"],["machine","learning","is","powerful"]]

model = Word2Vec(sentences=sentences,vector_size = 50,window=2,sg=0,min_count=1)

print(model.wv["learning"])   #represents meaning of 
print("-----------------------------------")
print(model.wv.most_similar("learning"))  # words ranked by similarity score


#if word is not present in the training it gives the error

#used to predict the single word based on context