#bubble sort
myList = [5, 2, 9, 1, 5, 6]
swapped = True

print("Unsorted list:", myList)

while swapped:
    swapped = False
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            myList[i], myList[i + 1] = myList[i + 1], myList[i]
            swapped = True

print("Sorted list:", myList)

#interactieve bubble sort
myList = []
panjang = int(input("Masukkan panjang list: "))

for i in range(panjang):
    angka = float(input(f"Masukkan angka ke-{i + 1}: "))
    myList.append(angka)

swapped = True
print("Unsorted list:", myList)

while swapped:
    swapped = False
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            myList[i], myList[i + 1] = myList[i + 1], myList[i]
            swapped = True

print("Sorted list:", myList)   

#method sort
mylist = [5, 2, 9, 1, 5, 6]
print("Unsorted list:", mylist)

mylist.sort()
print("Sorted list:", mylist)

#method reverse sort
mylist = [5, 2, 9, 1, 5, 6]
print("Unsorted list:", mylist)

mylist.reverse()
print("Reversed list:", mylist)

#the inner life of the list -1
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_1)

#slicing
mylist = [5, 2, 9, 1, 5, 6]
newlist = mylist[1:3]

print(newlist)

#slicing positif - negatif
mylist = [5, 2, 9, 1, 5, 6]
newlist = mylist[1:-1]
print(newlist)

#slicing negatif - positif
mylist = [5, 2, 9, 1, 5, 6]
newlist = mylist[-1:1]
print(newlist)

#slicing akhir
mylist = [5, 2, 9, 1, 5, 6]
newlist = mylist[:3]
print(newlist)

#slicing awal
mylist = [5, 2, 9, 1, 5, 6]
newlist = mylist[3:]
print(newlist)

#slicing [:]
mylist = [5, 2, 9, 1, 5, 6]
newlist = mylist[:]
print(newlist)

#slicing del
mylist = [5, 2, 9, 1, 5, 6]
del mylist[1:3]
print(mylist)

#slicing del all
mylist = [5, 2, 9, 1, 5, 6]
del mylist[:]
print(mylist)

#menghapus list
mylist = [5, 2, 9, 1, 5, 6]
del mylist
print(mylist)

#operator in
mylist = [5, 2, 9, 1, 5, 6]
print(5 in mylist)

#operator not in
mylist = [5, 2, 9, 1, 5, 6]
print(10 not in mylist)

#simple program 1
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

#simple program 2
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)

#simple program 3
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
   found = my_list [i] == to_find
   if found:
       break

if found:
    print(f"{to_find} ditemukan pada indeks {i}.")
else:
    print(f"{to_find} tidak ditemukan dalam list.")

#kuis 21
lotre = [3, 7, 11, 42, 34, 49]
lotreSudahKeluar = [5, 9, 11, 42, 3, 49]
tebakanBenar = 0

for angka in lotre:
    if angka in lotreSudahKeluar:
        tebakanBenar += 1

print(f"Jumlah tebakkan yang benar : {tebakanBenar}")

#kuis 22
sebuahList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
listSementara = []

for angka in sebuahList:
    if angka not in listSementara:
        listSementara.append(angka)
print(listSementara)