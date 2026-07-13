#Example 1
#using isdigit()

text = 'I have 2 dogs'
cleaned = ''.join(c for c in text if not c.isdigit())
print(cleaned)

# isdigit() fails for the decimal values


#EXample 2
import re

text2 = "I have 3 dogs"
cleaned11 = re.sub(r'\d+','',text)

print(cleaned11)


#Example 3
#using token filtering

text = "I have 3 dogs"
words = text.split()
filtered = [w for w in words if not w.isnumeric()]
print(filtered)

