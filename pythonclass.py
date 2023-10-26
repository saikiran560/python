class classname():
    name = "xyz"
    age = 25
    salary = 15000

    def __init__(self, name, age, salary):
        self.name = "name"
        self.age = "age"
        self.salary = "salary"

        def empdetails(self):
            print(self.name, self.age, self.salary)


empobj = classname()
empobj.name = "kiran"
# print(empobj.name,empobj.salary)