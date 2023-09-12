
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

print("Dictionary =",Dict)

del(Dict[1])
print("Data after deletion Dictionary=",Dict)



#dictionary methods
dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}

# copy()
dict2 = dict1.copy()
print(dict2)

# clear()
dict1.clear()
print(dict1)

# get()
print(dict2.get(1))

# items()
print(dict2.items())

# keys()
print(dict2.keys())

# pop() method
dict2.pop(4)
print(dict2)

# popitem() method
dict2.popitem()
print(dict2)

# update() method
dict2.update({3: "Scala"})
print(dict2)

# values() method
print(dict2.values())
