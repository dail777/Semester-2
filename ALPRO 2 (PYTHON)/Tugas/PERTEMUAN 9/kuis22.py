sebuahList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
listSementara = []

for angka in sebuahList:
    if angka not in listSementara:
        listSementara.append(angka)
print(listSementara)