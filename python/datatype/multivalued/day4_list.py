#list indexing

l = [10,20,30,40,50,60]

print(l)  # [10,20,30,40,50,60]
print(type(l))  #<class 'list'> 


#nested list
l2 = [1,3,3,5,[2,5,6], 6, 7]

print(l2[0]) # 1
print(l2[4][1])   # 5
print(l2[4][3])    #IndexError: list index out of range

#positive indexing
print(l[1])  # 20
print(l[3])  # 40
print(l[6])  # IndexError: list index out of range
print(l[0])  # 10
print(l[2])  # 30
print(l[7])  # IndexError: list index out of range


#negative indexing
print(l[-1])  # 60
print(l[-2])  # 50
print(l[-3])  # 40
print(l[-5])  # 20
print(l[-4])  # 30



#list slicing

l = [10,20,30,40,50,60,70]


#positive slicing
print(l[0::])    #[10, 20, 30, 40, 50, 60]
print(l[0:3:1]) # [10, 20, 30]

print(l[1:4:1]) # [20,30,40]

print(l[2:6:1]) # [30, 40, 50, 60]
print(l[3:7:1]) #[40, 50, 60, 70]
print(l[0:4:1]) # [10, 20, 30, 40]
print(l[0:7:2]) # [10, 30, 50, 70]
print(l[1:6:2]) # [20, 40, 60]
print(l[0:7:3])  #[10, 40, 70]

#negative slicing


l = [10,20,30,40,50,60,70]

print(l[-7:-4:1])   #[10, 20, 30]
print(l[-6:-3:1])    #[20, 30, 40]
print(l[-5:-2:1]) # [30, 40, 50]

print(l[-6:6:2]) # [20, 40, 60]

print(l[-4:-1:1]) # [40, 50, 60]
print(l[-7:7:2]) #[10, 30, 50, 70]
print(l[-5:6:1]) # [30, 40, 50, 60]
print(l[-4:6:1]) # [40, 50, 60]
print(l[-7:-1:1]) #[10, 20, 30, 40, 50, 60]


#reverse 

l = ['python', 10,44,50, 89,'smith',60,50]

print(l[6::-1])  #  [60, 'smith', 89, 50, 44, 10, 'python']
print(l[::-1])   #  [50, 60, 'smith', 89, 50, 44, 10, 'python']
print(l[6:0:-1])    # [60, 'smith', 89, 50, 44, 10]
print(l[5:1:-1])    # ['smith', 89, 50, 44]
print(l[4::-1])     # [89, 50, 44, 10, 'python']
print(l[6:2:-2])    # [60, 89]