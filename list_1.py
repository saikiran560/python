fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)


print(fruits.count("cherry"))


print(fruits.index("cherry"))

fruits.insert(1, "orange")
print(fruits)

fruits.pop(1)
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)

x = fruits.copy()
print(x)
