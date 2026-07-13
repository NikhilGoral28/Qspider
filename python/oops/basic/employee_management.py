class Company:
    company_name = 'pysiders'  #class variables

    def details(self,ename,cur_sal):   #object variables
        self.cur_sal = cur_sal
        self.ename = ename

    
    def increment(self,inc):
        if inc > 0:
            self.updated_sal = self.cur_sal+inc
        else:
            self.updated_sal = self.cur_sal
            print("increment should be greater than 0")
    


    def display(self):
        print()
        print(f">>>>> {self.company_name} <<<<<")
        print(f"Employee name: {self.ename}")
        print(f"Employee present Salary: {self.cur_sal}")
        print(f"Employee Updated Salary: {self.updated_sal}")


#object creation
e1 = Company()
e1.details('smith',50000)
e1.increment(98)
e1.display()
