import sqlite3

conn = sqlite3.connect(r'D:\Qspider\python\SQL_Connection\employee.db')

cursor = conn.cursor()

#create a table
cursor.execute('''
            CREATE TABLE IF NOT EXISTS EMP 
               (Empno integer primary key autoincrement,
               ename text,
               job text,
               sal real)            
''')


#add
def add():
    ename = input("Enter a Name: ")
    job = input("Enter a Job: ")
    sal = input("Enter a salary: ")

    cursor.execute('''
                    insert into emp (ename,job,sal) values (?,?,?), (ename,job,sal)
                   ''')
    
    conn.commit()
    print("Added!")


