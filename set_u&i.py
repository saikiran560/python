setA={1,2,3,33,55,63,4,5,6,7,8,9}
print(setA)
setB={4,5,6,33,9,67}
print(setB)

print(setB.issubset(setA))
print(setA.issuperset(setB))
print(setA.union(setB))


intersect=setA.intersection(setB)
print(intersect)

setDif=setB.difference(setA)
print(setDif)

setsyDif=setB.symmetric_difference(setA)
print(setsyDif)


