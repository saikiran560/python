def case(string):
    if string.isupper():
        return string.lower()
    if string.islower():
     return string.upper()
    else:
      return string

string = input("enter a stirng:")
str = case(string)
print(str)