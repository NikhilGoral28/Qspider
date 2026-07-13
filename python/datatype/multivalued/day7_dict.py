dic = {
    'a' : 10,
    'b' : 20,
    'c' : 30
}

print(dic)   # {'a': 10, 'b': 20, 'c': 30}
print(type(dic))  #<class 'dict'>

data  = {
    'ename' : 'smith',
    'sal' : 98000,
    'job' : 'Analyst'
}


print(data.keys())   #  dict_keys(['ename', 'sal', 'job'])
print(data.values())  # dict_values(['smith', 98000, 'Analyst'])

print(data.items())   # dict_items([('ename', 'smith'), ('sal', 98000), ('job', 'Analyst')])

#----------------------------------------------------------------------------------------------------------------

employee = {
    'emp1': {'ename' : 'smith', 'sal' : 98000},
    'emp2': {'ename' : 'martin', 'sal' : 95000},
    'emp3': {'ename' : 'scott', 'sal' : 45000},
    'emp4': {'ename' : 'allen', 'sal' : 38000},
    'emp5': {'ename' : 'james', 'sal' : 78000},
}


#wap to print employee 3 info
print(employee['emp3'])  # {'ename': 'scott', 'sal': 45000}

#wap to print name of third employee
print(employee['emp3']['ename'])   # scott


#wap to print employee 2 info
print(employee['emp2'])  # {'ename': 'martin', 'sal': 95000}


#wap to print employee 4th and 5th info
print(employee['emp4'],employee['emp5'])  # {'ename': 'allen', 'sal': 38000} {'ename': 'james', 'sal': 78000}


#wap to print name of the 4th employee and sal of the 5th emplyoyee
print(employee['emp4']['ename'], employee['emp5']['sal'])  # allen 78000


#printing all the keys
print(employee.keys())   # dict_keys(['emp1', 'emp2', 'emp3', 'emp4', 'emp5'])

#printin the employee 1 keys
print(employee['emp1'].keys())  # dict_keys(['ename', 'sal'])