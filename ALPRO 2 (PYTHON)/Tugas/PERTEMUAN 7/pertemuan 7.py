# ========================================================
# append & insert.py
# ========================================================
angka = [111, 7, 2, 1]
print(len(angka))
print(angka)

angka.append(4)

print(len(angka))
print(angka)

angka.insert(0, 222)
print(len(angka))
print(angka)

angka.insert(0, 333)
print(len(angka))
print(angka)


# ========================================================
# contoh 2 menggunakan list code 1.py
# ========================================================
my_list = []

for i in range(5):
    my_list.append(i + 1)
    
print(my_list)


# ========================================================
# contoh 2 menggunakan listcode 1.py
# ========================================================
my_list = []

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)


# ========================================================
# fungsi len.py
# ========================================================
listLust = ["apel", "jeruk", "mangga", "pisang", "anggur", 1, 2, 3, 4, 6]
print("List Awal:", listLust)
print("Panjang List:", len(listLust))

listLust.pop()
print("List setelah dihapus elemen terakhir:", listLust)
print("Panjang List setelah dihapus elemen terakhir:", len(listLust))


# ========================================================
# indexingList.py
# ========================================================
listNama = ["Andi", "Budi", "Citra", "Anto", "Devi"]
print("List Awal:", listNama)
nama = str(input("Masukkan nama: "))
ruang = int(input("Masukkan Ruang Ke Berapa Yang Akan Diubah: "))
listNama[ruang-1] = nama
print("List setelah ditambahkan nama:", listNama)


ruang = int(input("Masukkan Ruang Ke Berapa Yang Akan Dicopy: "))
ruang2 = int(input("Masukkan Ruang Ke Berapa Yang Akan Diisi: "))
listNama[ruang2-1] = listNama[ruang-1]
print(f"Ruang Ke-{ruang} telah dicopy ke Ruang Ke-{ruang2}")
print("List setelah dikopi:", listNama)


# ========================================================
# kuis 19.py
# ========================================================
topi_list = [1, 2, 3, 4, 5]
tengah = len(topi_list) // 2

angka = int(input("Masukkan angka: "))
topi_list.insert(tengah, angka)

topi_list.pop()
print("Panjang List : ", len(topi_list))

print(topi_list)


# ========================================================
# kuis 20.py
# ========================================================
exo = []

exo.append("Suho")
exo.append("Kai")
exo.append("Chanyeol")
exo.append("Sehun")

print(f"Anggota EXO: {exo}")

anggota_tambahan = ["DO", "Baekhyun", "Kris", "Lay", "Luhan", "Tao", "Chen"]
for anggota in anggota_tambahan:
    exo.append(anggota)
print(f"Anggota EXO Setelah Ditambah: {exo}")

exo.remove("Kris")
exo.remove("Luhan")
exo.remove("Tao")
print(f"Anggota EXO Setelah Dihapus: {exo}")

exo.insert(len(exo) - 2, "Xiumin")

print(exo)


# ========================================================
# list in action.py
# ========================================================
my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

for i in range(len(my_list) // 2):
    my_list[i], my_list[len(my_list) - 1 - i] = my_list[len(my_list) - 1 - i], my_list[i]

print("for looping :", my_list)

for i in range(100 // 2):
    my_list[i], my_list[len(my_list) - 1 - i] = my_list[len(my_list) - 1 - i], my_list[i]

print("for looping 2 :", my_list)


# ========================================================
# mengakses isi list.py
# ========================================================
hewan = ["kucing", "anjing", "burung", "ikan", "kelinci"]
print(hewan)
print(hewan[0])
print(hewan[1])
print(hewan[2])
print(hewan[3])
print(hewan[4])


# ========================================================
# menggunakan list code 2.py
# ========================================================
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print("Total:", total)


# ========================================================
# menggunakan list code1.py
# ========================================================
my_list = [10, 1, 8, 3, 5]
total = 0
for i in range(len(my_list)):
    total += my_list[i]

print(total)


# ========================================================
# menghapus elemen.py
# ========================================================
buah = ["apel", "jeruk", "mangga"]
print("List Awal:", buah)
del buah[0]
print("List setelah dihapus elemen pertama:", buah)


# ========================================================
# negative index.py
# ========================================================
ikan = ["ikan mas", "ikan lele", "ikan nila", "ikan gurame", "ikan patin"]
print(ikan[-2])
print(ikan[-1])
