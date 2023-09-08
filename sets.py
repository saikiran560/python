thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
print(len(thisset))
print(type(thisset))
for x in thisset:
 print(x)
print("banana" in thisset)
thisset.add("orange")

print(thisset)

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)

print(thisset)

mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


thisset.remove("banana")
print(thisset)

thisset.pop()
print(thisset)

#thisset.clear()
#print(thisset)

#del thisset
#print(thisset)

