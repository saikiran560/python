thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))
print(type(thistuple))
print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:5])
print(thistuple[:4])
y=list(thistuple)
y[1]="kiwi"
thistuple=tuple(y)
print(thistuple)
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
i = 0
while i < len(thistuple):
      print("using whileloop:",thistuple[i])
      i = i + 1
      