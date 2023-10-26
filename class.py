class abc :
    emp_name = "xyz"
    emp_age = 25
    emp_salary= 15000
    def em (self,emp,age,salary): 
        self.emp = input("nter name=")
        self.age = int(input("nter age="))
        self.salary = int(input("nter salary="))
    def emps(self):
        print("details\n", self.emp_name, self.emp_age, self.emp_salary)
    
pObj = abc()
pObj.emp_name= "mohan"
     

