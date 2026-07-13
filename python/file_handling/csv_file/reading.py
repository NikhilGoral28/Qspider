#without using the with statement for r mode

import csv

file = open(r'D:\Qspider\python\file_handling\csv_file\python.csv','r')
reader = csv.reader(file)
for row in reader:
    print(row)
file.close()


#using with statement for r mode

with open(r'D:\Qspider\python\file_handling\csv_file\python.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)



#for r+ mode without using with statemnt

file = open(r'D:\Qspider\python\file_handling\csv_file\python.csv','r+')
reader1 = csv.reader(file)
for rows in reader1:
    print(rows)

writter = csv.writer(file)      
writter.writerow(['ename','sal','deptno'])  
writter.writerow(['smith',900,20])
file.seek(0)

reader = csv.reader(file)
for row in reader:
        print(row)
file.close()


#for r+ mode using the with statement

with open(r'D:\Qspider\python\file_handling\csv_file\python.csv','r+') as file:

    reader = csv.reader(file)
    for row in reader:
        print(row)

    writter = csv.writer(file)      
    writter.writerow(['ename','sal','deptno'])    
    writter.writerow(['smith',900,20])
    file.seek(0)

    reader1 = csv.reader(file)
    for rows in reader1:
        print(rows)