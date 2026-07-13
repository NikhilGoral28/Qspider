#string to other datatypes

s1 = 'python'

print(list(s1))   # ['p', 'y', 't', 'h', 'o', 'n']
print(set(s1))    # {'n', 'o', 't', 'h', 'y', 'p'}
print(tuple(s1))  # ('p', 'y', 't', 'h', 'o', 'n')
print(bool(s1))   # True

#only converting the string gets a value error

print(int(s1))   # ValueError: invalid literal for int() with base 10: 'python'
print(float(s1))  # ValueError: could not convert string to float: 'python'
print(complex(s1)) # ValueError: complex() arg is a malformed string
print(dict(s1))  # ValueError: dictionary update sequence element #0 has length 1; 2 is required