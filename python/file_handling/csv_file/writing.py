#without using the with statement for w mode
import csv

file = open(r'D:\Qspider\python\file_handling\csv_file\python.csv','w')
writter = csv.writer(file)
writter.writerow(['ename','sal','deptno'])    #first row is considered as the column nane

writter.writerow(['smith',900,20])
file.close()



#for the w mode using with statement

with open(r'D:\Qspider\python\file_handling\csv_file\python.csv','w') as file:
    writter = csv.writer(file)
    writter.writerow(['ename','sal','deptno'])    #first row is considered as the column nane

    writter.writerows([['smith',900,20],
                       ['allen',800,10]])
    


#for the W+ mode without with statement


file = open(r'D:\Qspider\python\file_handling\csv_file\python.csv','w+')
writter = csv.writer(file)
writter.writerow(['ename','sal','deptno'])    #first row is considered as the column nane
writter.writerow(['king',900,20])
file.seek(0)
reader = csv.reader(file)

for row in reader:
    print(row)
file.close()


#for w+ mode using with statement

with open(r'D:\Qspider\python\file_handling\csv_file\python.csv','w+') as file:
    writter = csv.writer(file)      
    writter.writerow(['ename','sal','deptno'])    
    writter.writerow(['smith',900,20])
    file.seek(0)
    reader = csv.reader(file)

    for row in reader:
        print(row)
