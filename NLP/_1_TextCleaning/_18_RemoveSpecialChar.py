#Example 1

import re
text = "Hello @#$ NLP!!"

cleaned = re.sub(r'[^a-zA-Z\s|\d+]','',text)
print(cleaned)


#Example 2
import re

text = "Hello @#$ NLP!!"

cleaned = re.sub(r'[^a-zA-Z0-9\s]','',text)

print(cleaned)