#eception handling
try:
    a=int(input("enter the number : "))
    b=int(input("enter the number : "))
    print(a/b)
except:
    print('Some error occurred.')
print("Out of try except blocks.")
