class person:
    name = "kiran"
    age = 26
    gender = "male"
    def getdetails(self):
        self.name= input("enter the name")
        self.age=  int(input("enter the age"))
        self.gender= input("enter thr gender")
        self._persondetails()
 
    def _persondetails(self):
        print("Person details :\n",self.name , self.age ,self.gender)

pObj = person()
pObj.name="kiran"
pObj.age=25
pObj.getdetails()