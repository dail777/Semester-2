import sys
set_1 = {1,2,3,4,5}

tokenWord : set[int] = set({"Token"})
print(tokenWord)
print(sys.getsizeof(tokenWord))

print(set_1)
set_2 = {}
set_1.add(10)
print(set_1)
set_1.remove(2)
print(set_1)
set_1.remove(10)
print(set_1)
setlist = [set_1,set_2]
print(setlist)

#implementasi set dengan operasi matematika
#gabungan
setA = {1,2,3,4,5}
setB = {4,5,6,7,8}
setC = setA.union(setB)
print(setC)

#irisan
setD = setA & setB #atau setD = setA.intersection(setB)
print(setD)

#selisih
setE = setA - setB #atau setE = setA.difference(setB)
print(setE)
setF = setB - setA #atau setF = setB.difference(setA)
print(setF)

#selisih simetris
setG = setA ^ setB #atau setG = setA.symmetric_difference(setB)
print(setG)

