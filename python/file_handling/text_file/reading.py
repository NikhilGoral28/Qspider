#using the r mode

file = open(r'D:\Qspider\python\file_handling\pythonE18.txt','r')
display = file.read()
print(display)
file.close()



#using the r+ mode

#using the seek method

file = open(r'D:\Qspider\python\file_handling\pythonE18.txt','r+')
content  = file.write('writing file using the r+ mode')
file.seek(0)
display = file.read()
print(display)
file.close()


#without using the seek method

file = open(r'D:\Qspider\python\file_handling\pythonE18.txt','r+')
content  = file.write('writing file using the r+ mode')
file.close()

file = open(r'D:\Qspider\python\file_handling\pythonE18.txt','r+')
display = file.read()
print(display)
file.close()