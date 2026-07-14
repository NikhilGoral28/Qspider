from gensim.models import Word2Vec

sentences = [["deep","learning","is","fun"],["machine","learning","is","powerful"]]

model = Word2Vec(sentences=sentences,vector_size = 50,window=2,sg=1,min_count=1)

print(model.wv["learning"])  ##represents meaning of learning
print("-----------------------------------")  
print(model.wv.most_similar("learning"))  # words ranked by similarity score


##if word is not present in the training it gives the error
#used to predict the context based on single word