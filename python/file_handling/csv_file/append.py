#for a mode without using with statement
import csv

file = open(r'D:\Qspider\python\file_handling\csv_file\python.csv','a')
writter = csv.writer(file)      
writter.writerow(['king',5000,20])
file.seek(0)
file.close()


#for a mode using with statement

with open(r'D:\Qspider\python\file_handling\csv_file\python.csv','a') as file:
    writter = csv.writer(file)      

    writter.writerow(['scott',7000,20])



#for a+ mode without with statement

file = open(r'D:\Qspider\python\file_handling\csv_file\python.csv','a+')
reader1 = csv.reader(file)
for rows in reader1:
    print(rows)

writter = csv.writer(file)      
writter.writerow(['martin',400,10])
file.seek(0)

reader = csv.reader(file)
for row in reader:
        print(row)
file.close()


#for a+ mode using with statement

with open(r'D:\Qspider\python\file_handling\csv_file\python.csv','w+') as file:
    writter = csv.writer(file)      
    writter.writerow(['jones',1100,30])
    file.seek(0)
    reader = csv.reader(file)

    for row in reader:
        print(row)