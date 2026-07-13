#complex to other data types

#complex can only converts to boolean and str
a = 10 + 5j

print(str(a))   # (10+5j)
print(bool(a))  # True


print(int(a))   # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

#to collection datatypes gets type error

print(list(a))    #  TypeError: 'complex' object is not iterable
print(dict(a))    #  TypeError: 'complex' object is not iterable
print(tuple(a))   #  TypeError: 'complex' object is not iterable
print(set(a))    #  TypeError: 'complex' object is not iterable