#boolean to other data types

a = True

print(int(a))   # 1
print(complex(a))  # (1+0j)
print(str(a))   # True
print(float(a))  # 1.0


#to collection datatypes gets type error

print(list(a))    #  TypeError: 'bool' object is not iterable
print(dict(a))    #  TypeError: 'bool' object is not iterable
print(tuple(a))   #  TypeError: 'bool' object is not iterable
print(set(a))    #  TypeError: 'bool' object is not iterable