t = (10,20,30,40)
print(t)   #(10, 20, 30, 40)

print(type(t))  #<class 'tuple'>

t1 = 10,30,50,40
print(type(t1))  #<class 'tuple'>

t2 = (10)
print(type(t2))  #<class 'int'>

t3 = (10,)
print(type(t3))  #<class 'tuple'>


#indexing

t = (900,100,400,500,98,14,(1,2,3),'smith')

#positive indexing
print(t[1])  # 100
print(t[3]) # 500
print(t[0]) # 900
print(t[5]) # 14
print(t[9])  # IndexError: tuple index out of range

#negative indexing
print(t[-1])   # smith
print(t[-3])   #  14
print(t[-8])   # 900

print(t[-4])   # 98
print(t[-7])   # 100


#slicing

t = (900,100,400,500,98,14,(1,2,3),'smith')

#positive slicing
print(t[0:5:1])  #  (900, 100, 400, 500, 98)
print(t[1:7:1])   #  (100, 400, 500, 98, 14, (1, 2, 3))
print(t[2:8:2])   #  (400, 98, (1, 2, 3))
print(t[0:9:3])   #  (900, 500, (1, 2, 3))
print(t[3:9:2])   #  (500, 14, 'smith')
print(t[4:9:1])   #   (98, 14, (1, 2, 3), 'smith')
print(t[1:9:2])   #  (100, 500, 14, 'smith')
print(t[0:8:4])   #  (900, 98)
print(t[2:9:3])   #  (400, 14)
print(t[5:9:1])   #  (14, (1, 2, 3), 'smith')

#negative slicing

t = (900,100,400,500,98,14,(1,2,3),'smith','martin')

print(t[-9:-1:1])    # (900, 100, 400, 500, 98, 14, (1, 2, 3), 'smith')
print(t[-8:-2:1])   # (100, 400, 500, 98, 14, (1, 2, 3))
print(t[-7:-1:3])   #(400, 14)
print(t[-6:-2:1])   # (500, 98, 14, (1, 2, 3))
print(t[-5:-1:2])  #(98, (1, 2, 3))
print(t[-9:-3:2])  #(900, 400, 98)
print(t[-8:-1:1])   #(100, 400, 500, 98, 14, (1, 2, 3), 'smith')
print(t[-7:-3:2])   #(400, 98)
print(t[-6:-1:2])   # (500, 14, 'smith')
print(t[-4:-1:1])     # (14, (1, 2, 3), 'smith')


#reverse 
t = (900,100,400,500,98,14,(1,2,3),'smith','martin')

print(t[::-1])  #('martin', 'smith', (1, 2, 3), 14, 98, 500, 400, 100, 900)
print(t[2::-2])  # (400, 900)
print(t[-2::-2])  # ('smith', 14, 500, 100)

