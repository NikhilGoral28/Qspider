print('#-----------------------------------------------------------------------------------#')
print("BPE Tokenization")
print('#-----------------------------------------------------------------------------------#')

#Example 1 -- using BPE(byte pair encoding) method

from tokenizers import Tokenizer,models,pre_tokenizers,trainers
tokenizer = Tokenizer(models.BPE())

tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()
tokenizer.train(["data.txt"],trainers.BpeTrainer(vocab_size=50))
print(tokenizer.encode("lowest").tokens)


#Example 2

from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace

tokenizer = Tokenizer(BPE())
tokenizer.pre_tokenizer = Whitespace()
tokenizer.train(["data.txt"],trainers.BpeTrainer(vocab_size=50))
print(tokenizer.encode('lowest').tokens)



##################################################################################

print('\n\n#-----------------------------------------------------------------------------------#')
print("WordPiece Tokenization")
print('#-----------------------------------------------------------------------------------#')
#example 1 - Wordpiece method

from tokenizers import Tokenizer, models, pre_tokenizers, trainers
tokenizer = Tokenizer(models.WordPiece())
tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()
trainer = trainers.WordPieceTrainer(vocab_size=50,special_tokens=["[PAD]","[UNK]","[CLS]","[SEP]","[MASK]"])

tokenizer.train(['data.txt'],trainer)

print(tokenizer.encode("newest").tokens)



#Example 2

from tokenizers import Tokenizer,models , trainers
tokenizer = Tokenizer(models.WordPiece())
tokenizer.train(["data.txt"],trainers.WordPieceTrainer(vocab_size=50))
print(tokenizer.encode('lowest').tokens)

############################################################################################################33

print('\n\n#-----------------------------------------------------------------------------------#')
print("Uniform Tokenization")
print('#-----------------------------------------------------------------------------------#')

#Example 1

from tokenizers import Tokenizer, models,trainers
tokenizer = Tokenizer(models.Unigram())
tokenizer.train(['data.txt'],trainers.UnigramTrainer(vocab_size=50))
print(tokenizer.encode('lowest').tokens)


#Example 2

from tokenizers import Tokenizer,models,trainers

tokenizer = Tokenizer(models.Unigram())
trainer = trainers.UnigramTrainer(vocab_size=50)
tokenizer.train(['data.txt'],trainer)

print(tokenizer.encode('newest').tokens)





print('X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X')