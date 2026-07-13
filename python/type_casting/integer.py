#integer to other data types

a = 98

print(float(a))   # 98.0
print(complex(a))  # (98+0j)
print(str(a))   # 98
print(bool(a))  # True


#to collection datatypes gets type error

print(list(a))    #  TypeError: 'int' object is not iterable
print(dict(a))    #  TypeError: 'int' object is not iterable
print(tuple(a))   #  TypeError: 'int' object is not iterable
print(set(a))    #  TypeError: 'int' object is not iterable