#Example 1

import unicodedata

text = "Café naïve résumé São Tomé"

cleaned = unicodedata.normalize('NFKD',text).encode('ascii','ignore').decode('utf-8')

print(cleaned)


#Example 2

from unidecode import unidecode

text = "Café résumé"

cleaned = unidecode(text)
print(cleaned)