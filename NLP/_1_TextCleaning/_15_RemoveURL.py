#Example 1

import re

text = "Visit https://example.com"

cleaned = re.sub(r'http\S','',text)
print(cleaned)


#example 2

text = "Check wwww.google.com for more info"

cleaned = re.sub(r'www\S','',text)
print(cleaned)