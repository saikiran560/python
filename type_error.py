#Type Error
try:
  a=int(input("enter the number : "))
  b=int(input("enter the number : "))
  print(a+b)
except TypeError:
  print('TypeError Occurred')
except:
  print('Some error occurred.')  
print ("Out of try except blocks")