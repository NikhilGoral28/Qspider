#Example 1

text = "Hello  world"

cleaned = ''.join(text.split())
print(cleaned)


#Example 2

import re

text = "Hello    NLP"

cleaned = re.sub(r'\s','',text)
print(cleaned)


#split() removes the extra spaces
