#syntax error

number = 100

if number > 50
    print("Number is greater than 50!")

#if (number > 50):

#logical error

num = 30
z = num / 0

print(z)


#semantic error
a,b=3,4
a+b=c  # c= a+b
print(c)


#runtime error
 somelist=[1,2,3,4,5,6,7,8]
 print(somelist[9])



#eception handling
try:
    a=5
    b='0'
    print(a/b)
except:
    print('Some error occurred.')
print("Out of try except blocks.")


#Type Error
try:
  a=5
  b='0'
  print(a+b)
except TypeError:
  print('TypeError Occurred')
except:
  print('Some error occurred.')  
print ("Out of try except blocks")

#except and else 
try:
  x,y = 10,2
  z=x/y
except ZeroDivisionError:
  print("except ZeroDivisionError block")
  print("division by 0 not accepted")
except:
  print('Some error occurred.')
else:
  print("division = ", z)

print ("Out of try, except, else blocks." )

#raise exception
try:
  x,y=100,2
  z=x/2
  if z > 10:
    raise ValueError(z)
except ValueError:
  print(z, "is out of allowed range")
else:
  print(z, "is within the allowed range")










