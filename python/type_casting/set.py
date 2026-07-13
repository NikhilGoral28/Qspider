#set to other datatypes

s1 = {10,20,40,50,60}

print(str(s1))   # {10, 20, 40, 50, 60}
print(tuple(s1))    # (40, 10, 50, 20, 60)
print(list(s1))  #[10, 20, 40, 50, 60]
print(bool(s1))   # True


print(int(s1))   # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
print(float(s1))  # TypeError: float() argument must be a string or a real number, not 'set'
print(complex(s1)) #TypeError: complex() first argument must be a string or a number, not 'set'
print(dict(s1))  # TypeError: cannot convert dictionary update sequence element #0 to a sequence