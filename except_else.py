#except and else 
try:
  x=int(input("enter the number : "))
  y=int(input("enter the number : "))
  z=x/y
except ZeroDivisionError:
  print("except ZeroDivisionError block")
  print("division by 0 not accepted")
except:
  print('Some error occurred.')
else:
  print("division = ", z)

print ("Out of try, except, else blocks." )