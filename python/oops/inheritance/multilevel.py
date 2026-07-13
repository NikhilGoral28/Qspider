#employee

class employee:
    
    def __init__(self,empno,ename,salary):
        self.empno = empno
        self.ename = ename
        self.salary = salary

    def display_employee(self):
        print(f'Employee Number: {self.empno}')
        print(f'Employee Name: {self.ename}')
        print(f'Employee Salary: {self.salary}')


class Department(employee):

    def __init__(self,empno,ename,salary,dname):
        super().__init__(self,empno,ename,salary)
        self.dname = dname
    
    def display_department(self):
        self.display_employee()
        print(f'Department Name: {self.dname}')

'''
class Project(Department):
    def __init__(self, empno, ename, salary, dname,pid,project_name):
        super().__init__(empno, ename, salary, dname)
        self.pid = pid
        self.project_name = project_name
    
    def display_Project(self):
        self.display_department()
        print(f"Project Id: {self.pid}")
        print(f'Project Name: {self.project_name}') 

'''

e1 = Department(12,'SMITH', 89988,23)
e1.display_department()