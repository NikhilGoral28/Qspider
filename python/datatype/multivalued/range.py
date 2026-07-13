

r1 = range(11)
print(r1)   # range(0, 11)

r2 = range(11)
print(list(r2))   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


r3 = range(6)
print(tuple(r3))  # (1,2,3,4,5)


#example for start and stop

r4 = range(1,11)
print(list(r4))  # [1,2,3,4,5,6,7,8,9,10]


#example for start, stop, step

r5 = range(1,7,1)
print(list(r5))  # [1,2,3,4,5,6]

r6 = range(10,101,10)
print(list(r6))  # [10,20,30,40,50.60,70,90,100]

r7 = range(1,7,2)
print(list(r7))  # [1,3,5]

#example for start, stop, step  -- desending order

r1 = range(10,0,-1)
print(list(r1))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

r2 = range(10,0,-2)
print(list(r2))  # [10, 8, 6, 4, 2]



#indexing 

r1 = range(10,101,10)
updated = list(r1)


print(updated[1])   # 20
print(updated[0])   # 10
print(updated[8])   # 90
print(updated[6])   # 70
print(updated[4])   # 50
print(updated[11])  # IndexError: list index out of range
print(updated[-1])  # 100
print(updated[-2])  # 90
print(updated[-3])  # 80
print(updated[-6])  # 50
print(updated[-9])  # 20


#slicing 

#positive slicing

r1 = range(10,101,10)
updated = list(r1)

print(updated[0:5])     # [10, 20, 30, 40, 50]
print(updated[2:7])     # [30, 40, 50, 60, 70]
print(updated[1:9:2])   # [20, 40, 60, 80]
print(updated[:5])      # [10, 20, 30, 40, 50]
print(updated[5:])      # [60, 70, 80, 90, 100]
print(updated[4:9:2])   # [50, 70, 90]


#negative slicing

r1 = range(10,101,10)
updated = list(r1)


print(updated[-1])        # 100
print(updated[-5:-1])     # [60, 70, 80, 90]
print(updated[-7:-2])     # [40, 50, 60, 70, 80]
print(updated[-10:-5])    # [10, 20, 30, 40, 50]
print(updated[-8:])       # [30, 40, 50, 60, 70, 80, 90, 100]
print(updated[:-3])       # [10, 20, 30, 40, 50, 60, 70]
print(updated[-9:-1:2])   # [20, 40, 60, 80]



#reverse

r1 = range(10,101,10)
updated = list(r1)


print(updated[::-1])      # [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
print(updated[5:0:-1])    # [60, 50, 40, 30, 20]
print(updated[9:5:-1])    # [100, 90, 80, 70]
print(updated[-4:-8:-1])  # [70, 60, 50, 40]
print(updated[5:2:-1])   # [60, 50, 40]
print(updated[::-2])    # [100, 80, 60, 40, 20]


