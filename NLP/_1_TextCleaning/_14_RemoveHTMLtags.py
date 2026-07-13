#Example 1 using re

import re

text = "<p>This is NLP</p>"

cleaned =re.sub(r'<.*?>','',text)

print(cleaned)


#Example 2

from bs4 import BeautifulSoup

text = "<div>This is NLP</div>"

cleaned = BeautifulSoup(text,"html.parser").get_text()
print(cleaned)