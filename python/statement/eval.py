num = eval(input("enter a value"))
print(type(num))  # <class 'int'>


result = eval('2'+'2')
print(type(result))   # <class 'int'>
print(result)   # 22


result = eval('2+2')
print(result)        # 4
print(type(result))  # <class 'int'>