#example 1

import re

text = "I love NLP 😊🔥"
cleaned = re.sub(r'[^\w\s]','',text)
print(cleaned)


#Example 2 using Emoji

import emoji

text = "I love NLP 😊🔥"

cleaned = emoji.replace_emoji(text,replace='')
print(cleaned)

#Example 3  convert to text

text = "I love NLP 😊"
cleaned = emoji.demojize(text)

print(cleaned)