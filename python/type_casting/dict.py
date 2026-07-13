#dict to other datatypes

data= {'ename':'smith','sal':98000}

print(str(data))   # {'ename': 'smith', 'sal': 98000}
print(tuple(data))    # ('ename', 'sal') --- only keys
print(list(data))  # ['ename', 'sal']  --- only keys
print(bool(data))   # True
print(set(data))  # {'ename', 'sal'} --- only keys


print(int(data))   # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
print(float(data))  # TypeError: float() argument must be a string or a real number, not 'dict'
print(complex(data)) #TypeError: complex() first argument must be a string or a number, not 'dict'