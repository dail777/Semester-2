#list comprehension
genap = [x for x in range(10) if x % 2 == 0 and x != 0]
print(genap)

#array 2 dimensi
papanCatur = [[i for i in range(8)] for j in range(8)]

papanCatur[1][2] = "Kuda"
papanCatur[6][5] = "Benteng"
papanCatur[0][0] = "Raja"
print(papanCatur)

#array multidimensi
jadwal = [
    ["Matematika", "Informatika", "Sejarah", "Olahraga", "Bahasa Jepang"],
    ["Bahasa Indonesia", "Fisika", "Geografi", "Seni Budaya", "Bahasa Korea"],
]

hari = ["Senin", "Selasa"]

for i in range(2):  # hari
    print(hari[i] + " :")
    for j in range(5):  # mapel
        print("-", jadwal[i][j])
    print()

#fungsi berparameter
def biografi(nama, umur, hobi, asal, pekerjaan):
    print("Nama saya adalah", nama)
    print("Umur saya adalah", umur, "tahun")
    print("Hobi saya adalah", hobi)
    print("Saya berasal dari", asal)
    print("Pekerjaan saya adalah", pekerjaan)

inputNama = input("Masukkan nama: ")
inputUmur = input("Masukkan umur: ")
inputHobi = input("Masukkan hobi: ")
inputAsal = input("Masukkan asal: ")
inputPekerjaan = input("Masukkan pekerjaan: ")

biografi(inputNama, inputUmur, inputHobi, inputAsal, inputPekerjaan)

#kuis 1
bilangan = [x for x in range(1, 11)]
bilangan_genap = [x for x in bilangan if x % 2 == 0]
bilangan_genap_kali_3 = [x * 3 for x in bilangan_genap]

print(bilangan)
print("Bilangan genap 1-10:", bilangan_genap)
print("Bilangan genap 1-10 dikali 3:", bilangan_genap_kali_3)

#kuis 2
array3x3 = [[i * 3 + j for j in range(1, 4)] for i in range(3)]
print(array3x3)

#kuis 3
data = [[2, 4], [6, 8], [10, 12]]

flatten = []
for angka in data:
    for isi in angka:
        flatten.append(isi)

print("Data:", data)
print("Data flatten:", flatten)

#kuis 4
def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas

hasil = hitung_luas_persegi_panjang(8, 5)
print(f"Luas persegi panjang : {hasil}")
