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
