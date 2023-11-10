#raise exception
try:
  x=int(input("enter the number : "))
  y=int(input("enter the number : "))
  z=x/y
  if z > 10:
    raise ValueError(z)
except ValueError:
  print(z, "is out of allowed range")
else:
  print(z, "is within the allowed range")


