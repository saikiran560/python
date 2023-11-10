fruits = {"apple", "banana", "cherry"}

fruits.add("orange")


print(fruits)

fruits.pop()

print(fruits)

fruits.remove("banana")

print(fruits)

d = fruits.copy()

print("copied set",d)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print("differece is :",z)

x.update(y)

print(x)
z = x.union(y) 
print(z)

x.difference_update(y) 

print(x)
