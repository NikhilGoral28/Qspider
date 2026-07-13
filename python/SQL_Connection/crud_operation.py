
#for creating tables
import sqlite3


#creating connection
conn = sqlite3.connect(r'D:\Qspider\python\SQL_Connection\demo.db')

#creating cursor
cur = conn.cursor()

#exectuing query

cur.execute(''' create table emp (
empno integer,
ename text, 
sal real)
            ''')

conn.commit()
conn.close()



#for inserting values

import sqlite3


#creating connection
conn = sqlite3.connect('demo1.db')

#creating cursor
cur = conn.cursor()

cur.execute('''
    insert into emp (empno,ename,sal)
    values (1234,'smith',98000)
''')


conn.commit()
conn.close()



#for display the values

import sqlite3


#creating connection
conn = sqlite3.connect('demo1.db')

#creating cursor
cur = conn.cursor()

cur.execute('select * from emp')
rows = cur.fetchall()

for row in rows:
    print(row)

conn.commit()
conn.close()


#for updating 

import sqlite3


#creating connection
conn = sqlite3.connect('demo.db')

#creating cursor
cur = conn.cursor()

#exectuing query

cur.execute('''
             update table emp set sal = 98000 where ename = 'king'        
''')

conn.commit()
conn.close()


#for delete

import sqlite3


#creating connection
conn = sqlite3.connect('demo.db')

#creating cursor
cur = conn.cursor()

#exectuing query

cur.execute('''
        delete from emp where ename = 'smith'
''')

conn.commit()
conn.close()
