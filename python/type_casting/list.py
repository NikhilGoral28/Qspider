#list to other datatypes

l1 = [10,20,40,50,60]

print(str(l1))   # [10, 20, 40, 50, 60]
print(set(l1))    # {40, 10, 50, 20, 60}
print(tuple(l1))  # (10, 20, 40, 50, 60)
print(bool(l1))   # True


print(int(l1))   # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
print(float(l1))  # TypeError: float() argument must be a string or a real number, not 'list'
print(complex(l1)) #TypeError: complex() first argument must be a string or a number, not 'list'
print(dict(l1))  # TypeError: cannot convert dictionary update sequence element #0 to a sequence