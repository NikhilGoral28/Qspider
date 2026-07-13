

#using the w mode

file = open(r'D:\Qspider\python\file_handling\pythonE18.txt','w')
content = file.write("This is a python demo file")
file.close()




#using the w+ mode 

#using seek method

file = open(r'D:\Qspider\python\file_handling\pythonE18.txt','w+')
content  = file.write('writing file using the w+ mode')
file.seek(0)
display = file.read()
print(display)
file.close()


#without using the seek method

file = open(r'D:\Qspider\python\file_handling\pythonE18.txt','w+')
content  = file.write('writing file using the w+ mode')
file.close()

file = open(r'D:\Qspider\python\file_handling\pythonE18.txt','w+')
display = file.read()
print(display)
file.close()

