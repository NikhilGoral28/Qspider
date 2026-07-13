#tuple to other datatypes

t1 = (10,20,40,50,60)

print(str(t1))   # (10, 20, 40, 50, 60)
print(set(t1))    # {40, 10, 50, 20, 60}
print(list(t1))  #[10, 20, 40, 50, 60]
print(bool(t1))   # True


print(int(t1))   # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
print(float(t1))  # TypeError: float() argument must be a string or a real number, not 'tuple'
print(complex(t1)) #TypeError: complex() first argument must be a string or a number, not 'tuple'
print(dict(t1))  # TypeError: cannot convert dictionary update sequence element #0 to a sequence