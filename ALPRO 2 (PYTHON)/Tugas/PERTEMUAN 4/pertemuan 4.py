# ========================================================
# fungsi input.py
# ========================================================
#user memasukan data untuk ditampilkan
text = input("Masukan kalimat untuk ditampilkan : ")
print("Kalimat :", text)


# ========================================================
# Input Dengan Argumen.py
# ========================================================
nim = input("Masukan NIM :")
nama = input("Masukan Nama :")

print("NIM :", nim)
print("Nama :", nama)


# ========================================================
# Input Kemudian ditampilkan.py
# ========================================================
#User input text untuk ditampilkan
pesan = input("Masukan Pesan : ")
print("Pesan :", pesan)


# ========================================================
# konversi menggunakan input.py
# ========================================================
#Input data int
angkaInt = int(input("Masukan Angka 1 Yang Akan Dikonversi :"))
angkaInt2 = int(input("Masukan Angka 2 Yang Akan Dikonversi :"))
#Konversi tipe Int ke Float
angkaFloat = float(angkaInt)
angkaFloat2 = float(angkaInt2)

#Membagi angka 1 dan 2 yang sudah bertipe float
operasiPembagian = angkaFloat / angkaFloat2

#menampilkan hasil input
print("Angka1 Bertipe Int :", angkaInt)
print("Angka2 Bertipe Int :", angkaInt2)
print("Konversi Angka1 ke Tipe FLoat :", angkaFloat)
print("Konversi Angka2 ke Tipe Float :", angkaFloat2)

print("Hasil Pembagian Angka Float 1 dan Angka Float 2 :", operasiPembagian)


# ========================================================
# konversi tipe string.py
# ========================================================
#data bertipe int
angka = int(input("Masukan Angka : "))
#konversi ke tipe string
angka_string = str(angka)
print("Angka yang anda input : ", angka_string)


# ========================================================
# kuis 7.py
# ========================================================
#User masukan angka a dan b
a = int(input("Masukan Nilai a : "))
b = int(input("Masukan Nilai b : "))

#operasi pejumlahan
print("Hasil penjumlahan a + b : ", a + b)
#operasi ppengurangan
print("Hasil pengurangan a - b : ", a - b)
#operasi pemabagian
print("Hasil pembagian a / b : ", a / b)
#operasi perkalian
print("Hasil perkalian a * b : ", a * b)

print("Selamat kamu sudah pintar matematika")


# ========================================================
# kuis 8.py
# ========================================================
#user menginputkan nilai x
x = float(input("Masukkan niai x : "))

#operasi nilai y
y = 1.0 / x + 1.0 / x + 1.0 / x + 1.0 / x

print("Hasil operasi y :", y)


# ========================================================
# kuis 9.py
# ========================================================
jam = int(input("Waktu Mulai (jam) : "))
waktu = int(input("Waktu Mulai (menit) : "))
durasi = int(input("Durasi Acara (menit) : "))

total_menit = waktu + durasi
jam_selesai = jam + (total_menit // 60)
menit_selesai = total_menit % 60

print(f"Acara selesai pukul {jam_selesai}:{menit_selesai}")


# ========================================================
# melihat tipe data dari suatu variable.py
# ========================================================
# Melihat tipe data dari suatu variable

# Contoh variable dengan berbagai tipe data
nama = "John"
umur = 25
tinggi = 175.5

# Menggunakan type() untuk melihat tipe data
print(f"Tipe data 'nama':", type(nama))
print(f"Tipe data 'umur':", type(umur))
print("Tipe data 'tinggi':", type(tinggi))


# ========================================================
# operator konkatenasi.py
# ========================================================
# Program Operator Konkatenasi dengan Input

nama = input("Masukkan nama Anda: ")
kota = input("Masukkan kota asal Anda: ")
pekerjaan = input("Masukkan pekerjaan Anda: ")

# Konkatenasi menggunakan operator +
hasil1 = "Nama saya adalah " + nama + " dan saya berasal dari " + kota

# Konkatenasi dengan menggabungkan beberapa string
hasil2 = nama + " bekerja sebagai " + pekerjaan

print(hasil1)
print(hasil2)


# ========================================================
# operator replikasi.py
# ========================================================
# Operator Replikasi dengan String
print("=== Operator Replikasi String ===")
nama = "Python "
hasil_string = nama * 3
print(f"'{nama}' * 3 = '{hasil_string}'")


# ========================================================
# program untuk menghitung luas segitiga  menggunakan rumus pythagoras.py
# ========================================================
import math

# Menghitung sisi miring segitiga menggunakan rumus Pythagoras
# Input sisi-sisi segitiga
sisi_a = float(input("Masukkan panjang sisi a: "))
sisi_b = float(input("Masukkan panjang sisi b: "))

# Rumus Pythagoras: c² = a² + b²
hypo = math.sqrt(sisi_a**2 + sisi_b**2)

print(f"Sisi miring (hipotenusa) = {hypo}")


# ========================================================
# program untuk menghitung menggunakan rumus pythagoras tanpa menggunakan variable.py
# ========================================================
import math

# Menghitung sisi miring segitiga menggunakan rumus Pythagoras
# Input sisi-sisi segitiga
sisi_a = float(input("Masukkan panjang sisi a: "))
sisi_b = float(input("Masukkan panjang sisi b: "))

print("Sisi miring (hipotenusa) :", math.sqrt(sisi_a**2 + sisi_b**2))
