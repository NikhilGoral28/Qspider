print("Hello World")  #Hello World

print("Welcome to python class")   #welcome to the python class

print("Tata tata bye bye")  # Tata tata bye bye


#printing all the keywords
import keyword
print(keyword.kwlist)


['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if',
  'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


#total keywords present in the python
print(len(keyword.kwlist))  #35


#checking the keyword is valid or not
                                                                                        
print(keyword.iskeyword("continue"))  #True
print(keyword.iskeyword('if'))   #True
print(keyword.iskeyword('elif'))    # True
print(keyword.iskeyword("Else"))   #False


#identifiers

name = 'king'
print(name)  #king

age = 23
print(age)   #23

ename_123 = 'SMITH'
print(ename_123)  #SMITH


#chekcing the identifier is valid or not
print(name.isidentifier())  #True
print(age.isidentifier())   #False

#variables

#single value variables 
ename = 'scott'

print(ename)   #scott


a = 34
print(a)  #34

sal = 34000
print(sal)   #34000

#multi value variables

a,b = 200, 100

print(a,b)   # 200 100

ename, salary = 'smith' , 98000

print(ename)  #smith
print(salary)  #98000


#escape sequence

print('hello\nPython')
    
    #hello
    #python

print("hello\nstudents\nwelome to the pyspider")

    #hello
    #student
    #welcome to pyspider


#string formating

ename = 'smith'

print(f'employee name {ename}')  # employeee name  smith


ename = 'king'
salary = 5000

print(f'Employee name is {ename} and he is earing salary {salary}') #Employee name is king and he is earning salary 5000