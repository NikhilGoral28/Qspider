s = {10,20,30,40}
print(s)  #{10,20,30,40}

print(type(s))  # <class 'set'>

#indexing and slicing can be perform using the type casting

l = list(s)

print(type(l))   # <class 'list'>

#indexing

print(l[0])     # possible output 40
print(l[1])    # possible output 10
print(l[-1])  # possible output 30


#slicing

print(l[1:5:1])  # [10, 20, 30]

