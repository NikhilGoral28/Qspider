#float to other data types

a = 98.56

print(int(a))   # 98
print(complex(a))  # (98.56+0j)
print(str(a))   # 98.56
print(bool(a))  # True


#to collection datatypes gets type error

print(list(a))    #  TypeError: 'float' object is not iterable
print(dict(a))    #  TypeError: 'float' object is not iterable
print(tuple(a))   #  TypeError: 'float' object is not iterable
print(set(a))    #  TypeError: 'float' object is not iterable