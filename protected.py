class myclass:
     def __init__(self):
           self.__protect_var = 60
     def __protected(self):
        return "protected method"
obj=myclass()
print(obj._myclass__protect_var)
print(obj._myclass__protected())