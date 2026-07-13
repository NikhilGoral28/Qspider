#module -- string.punctuation



#Example 1

import string

text = "Hello!!! How are you??"

cleaned = "".join(c for c in text if c not in string.punctuation)
print(cleaned)

#Explanation
#-- iterates char by char
#-- Removes char in string.punctuation


#Example 2

import re

text1 = "NLP, AI & ML are amazing"
cleaned1 = re.sub(r'[^\w\s]','',text1)
                  
print(cleaned1)
