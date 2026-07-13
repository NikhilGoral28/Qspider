#using the a mode

file = open(r'D:\Qspider\python\file_handling\pythonE18.txt','a')
content  = file.write('/n adding new data using a mode')
file.close()



#using the a+ mode

#with using the seek method

file = open(r'D:\Qspider\python\file_handling\pythonE18.txt','a+')
content  = file.write('\nadding data using a+ mode')
file.seek(0)
display = file.read()
print(display)
file.close()


#without using the seek method

file = open(r'D:\Qspider\python\file_handling\pythonE18.txt','a+')
content  = file.write('\n adding data using the a+ mode')
file.close()

file = open(r'D:\Qspider\python\file_handling\pythonE18.txt','a+')
display = file.read()
print(display)
file.close()


#tell method

#tell method is used to display the current position of the cursor

file = open(r'D:\Qspider\python\file_handling\pythonE18.txt','w+')
content  = file.write('writing file using the w+ mode')
file.seek(0)
display = file.read()
print(display)
file.close()


#without using the seek method

file = open(r'D:\Qspider\python\file_handling\pythonE18.txt','w+')
display = file.read()
print(display)
position = file.tell()
print(f'position of the cursor is {position}')
file.close()