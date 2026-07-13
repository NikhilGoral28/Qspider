
#addition 

print(100+200)  # 300
print('100'+'200') #100200
print('hello'+199)  # type error
print(98+True)   #99
print('hello'+' smith')  # hello smith


a = 10
b = 20
print(a+b)   # 30

a = 10 
b = 45 
sum = a+ b
print(sum)  #55


s1 = 'qspider'
s2 = 'jspider'
s3 = 'pyspider'
s4 = 'gspider'

print(s1+s2+s3+s4)   #qspiderjspiderpyspidergspider


l1 = [10,20,30]
l2 = [40,50,60]

result = l1 + l2
print(result)   # [10, 20, 30, 40, 50, 60]


t1 = (1,2,3)
t2 = (4,5,6)

result = t1+t2
print(result)   # (1, 2, 3, 4, 5, 6)

a = 98
b = 100 + 4j
result = a + b
print(result)  # (198+4j)


l1 = [10,20,30]
t1 = (1,2,3)

result = l1+t1
print(result)  # TypeError: can only concatenate list (not "tuple") to list

s1= {10,20,30}
s2 = {30,40}
result = s1+s2
print(result)  # TypeError: unsupported operand type(s) for +: 'set' and 'set'

#------------------------------------------------------------------------------------------------------------------------------------------------------

#substraction

a = 200
b= 100

print(a-b) # 100

a = 98
b = 45.5
print(a-b) # 52.5

s1 = 'smith'
s2 = 'scott'
print(s1-s2)  # TypeError: unsupported operand type(s) for -: 'str' and 'str'



l1 = [10,20,30]
l2 = [40,50,60]

print(l2-l1)  # TypeError: unsupported operand type(s) for -: 'list' and 'list'

#----------------------------------------------------------------------------------------------------------------------------------------------------

#multiplication


print(3*2)  # 6
print(3*' python') #python python python
print(2*[10,20])  # [10, 20, 10, 20]
print(4*(10,20))  # (10, 20, 10, 20, 10, 20, 10, 20)

print(2*{10,20})  # TypeError: unsupported operand type(s) for *: 'int' and 'set'
print(2*{'ename':'smith'})  # TypeError: unsupported operand type(s) for *: 'int' and 'dict'

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#true division

a = 98
b = 45

print(a/b) # 2.1777777777777776

a = 6
b = 3

print(a/b) # 2.0

#-------------------------------------------------------------------------------------------------------

a = 98
b = 45

print(a//b)  # 2

a = 39
b = 3
print(a//b) # 13

a = 48.98
b = 23.45

print(a//b) # 1.0


#wap to remove last digit of the given number

num = 98866
print(num//10)  # 9886

#wap to remove the last two digit from number

num = 2345352
print(num//100)  # 23453

# wap to remove last three digit from given number

num = 834465683
print(num//1000) #834465

#-----------------------------------------------------------------------------------------------------------------------------

#modulus

a = 11
b = 2

print(a%b) # 1

a = 10
b = 2
print(a%b)  # 0


#wap to display last digit from given number

num = 223423
print(num%10) # 3

#wap to print last two digits from given number

num = 8238873
print(num%100) #73

#wap to print last 4 digits from given number

num = 23435353
print(num%10000) # 5353

#--------------------------------------------------------------------------------------------------------------------------------------------

#exponent (**) -- power

print(2**3) #8

l = [3,2,3,4]
print(l**2)  # TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
