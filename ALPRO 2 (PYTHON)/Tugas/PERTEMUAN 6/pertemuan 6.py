# ========================================================
# binary shifting.py
# ========================================================
angka = 20
angkaKanan = angka >> 2 # dibagi 4
angkaKiri = angka << 2 # dikali 4
print("Angka Awal :", angka)
print("Hasil Shifting Kanan :", angkaKanan)
print("Hasil Shifting Kiri :", angkaKiri)


# ========================================================
# contoh break dan continue.py
# ========================================================
for i in range(1, 6):
    if i == 3:
        break
    print(f"INI DALAM LOOP : {i}")
print("INI DILUAR LOOP")

for i in range(1, 6):
    if i == 3:
        continue
    print(f"INI DALAM LOOP : {i}")
print("INI DILUAR LOOP")


# ========================================================
# ekspresi logika.py
# ========================================================
i = 1
j = not not i
print(j)


# ========================================================
# kuis 15.py
# ========================================================
secret_number = 777

text1 = "Selamat datang di game saya muggle!"
text2 = "masukkan suatu angka dan tebak"
text3 = "angka berapa yang saya pilih"
text4 = "untuk kamu."
text5 = "Jadi, berapa angka rahasianya?"

print("+" + "=" * 42 + "+")
print(f"| {text1.ljust(40)} |")
print(f"| {text2.ljust(40)} |")
print(f"| {text3.ljust(40)} |")
print(f"| {text4.ljust(40)} |")
print(f"| {text5.ljust(40)} |")
print("+"+"=" * 42 + "+")

angka_tebakan = int(input("Masukan angka tebakan : "))
while angka_tebakan != secret_number:
    print("hahaha! kamu nyangkut deh di Loop saya")
    angka_tebakan = int(input("Masukan angka tebakan : "))
else :
    print("Selamat, Muggle! kamu bebas sekarang!")


# ========================================================
# kuis 16.py
# ========================================================
secret_number = 777

text1 = "Selamat datang di game saya muggle!"
text2 = "masukkan suatu angka dan tebak"
text3 = "angka berapa yang saya pilih"
text4 = "untuk kamu."
text5 = "Jadi, berapa angka rahasianya?"

print("+" + "=" * 42 + "+")
print(f"| {text1.ljust(40)} |")
print(f"| {text2.ljust(40)} |")
print(f"| {text3.ljust(40)} |")
print(f"| {text4.ljust(40)} |")
print(f"| {text5.ljust(40)} |")
print("+"+"=" * 42 + "+")

angka_tebakan = int(input("Masukan angka tebakan : "))
while angka_tebakan != secret_number:
    print("hahaha! kamu nyangkut deh di Loop saya")
    angka_tebakan = int(input("Masukan angka tebakan : "))
    if angka_tebakan == secret_number:
        break

print("Selamat, Muggle! kamu bebas sekarang!")


# ========================================================
# kuis 17.py
# ========================================================
kataInput = str(input("Masukan kata : "))
user_word = kataInput.upper()

for kata in range(len(user_word)):
    kata = user_word[kata]
    if kata == "A" or kata == "I" or kata == "U" or kata == "E" or kata == "O":
        continue
    print(kata)


# ========================================================
# kuis 18.py
# ========================================================
x = 4
y = 1

a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)


# ========================================================
# menghitung angka ganjil dan genap menggunakan while.py
# ========================================================
angkaGanjil = 0
angkaGenap = 0

angka = int(input("Masukan Angka (0 untuk keluar) : "))
while angka != 0:
    if angka % 2 == 1:
        angkaGanjil += 1
    else:
        angkaGenap += 1
    angka = int(input("Masukan Angka (0 untuk keluar) : "))

print(f"Jumlah Angka Ganjil : {angkaGanjil}")
print(f"Jumlah Angka Genap : {angkaGenap}")


# ========================================================
# menghitung exponensial.py
# ========================================================
power = 1
angka = int(input("Masukan Angka Untuk Melihat Perpangkatan 0-10: "))
for expo in range(11):
    print(f"{angka} pangkat {expo} adalah {power}")
    power *= angka


# ========================================================
# operasi logical vs. bitwise.py
# ========================================================
i = 15
j = 22

log = i and j
bit = i & j

print(f"log : {log:b}")
print(f"bit : {bit:b}")

logneg = not i
bitneg = ~i

print(f"logneg : {logneg:b }")
print(f"bitneg : {bitneg:b}")


# ========================================================
# perbandingan abcde.py
# ========================================================
for a in range(10):
    print(f"nilai a : {a}")
for b in range(2, 8):
    print(f"nilai b : {b}")
for c in range(2, 8, 3):
    print(f"nilai c : {c}")
for d in range(1, 1):
    print(f"nilai d : {d}")
for e in range(2, 1):
    print(f"nilai e : {e}")


# ========================================================
# perulangan dengan while.py
# ========================================================
angka = int(input("Masukan Angka : "))
daftarAngka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0
while counter < len(daftarAngka):
    if daftarAngka[counter] == angka:
        print(f"Angka ditemukan dalam Ruang ke-{counter}.")
        break
    print(f"Ruang ke-{counter} sudah diperiksa.")
    counter += 1
    print(f"Mencari di Ruang ke-{counter}...")
else:
    print("Angka tidak ditemukan dalam daftar.")


# ========================================================
# perulangan while contoh 2.py
# ========================================================
nilaiA = 0
nilaiB = 0
nilaiC = 0
nilaiD = 0

nilai = str(input("Masukan Index Nilai Mahasiswa (A/B/C/D) ATAU EXIT UNTUK KELUAR : "))
while True:
    if nilai == "A" or nilai == "a":
        nilaiA += 1
    elif nilai == "B" or nilai == "b":
        nilaiB += 1
    elif nilai == "C" or nilai == "c":
        nilaiC += 1
    elif nilai == "D" or nilai == "d":
        nilaiD += 1
    elif nilai == "EXIT" or nilai == "exit":
        break
    else:
        print("Silakan masukkan A, B, C, D, atau EXIT untuk keluar.")

    nilai = str(input("Masukan Index Nilai Mahasiswa (A/B/C/D) ATAU EXIT UNTUK KELUAR : "))

print(f"Jumlah Nilai A : {nilaiA}")
print(f"Jumlah Nilai B : {nilaiB}")
print(f"Jumlah Nilai C : {nilaiC}")
print(f"Jumlah Nilai D : {nilaiD}")


# ========================================================
# while-else & for-else.py
# ========================================================
jumlahAkun = 0
akun : list = []

akun_input = str(input("Masukan Nama Akun Batas 5 Akun Untuk diinput (Ketik 'EXIT' untuk keluar) : "))
while akun_input != "EXIT" and akun_input.lower() != "exit":
    if akun_input == "EXIT" or akun_input.lower() == "exit":
        break
    akun.append(akun_input)
    jumlahAkun += 1
    akun_input = str(input("Masukan Nama Akun Batas 5 Akun Untuk diinput (Ketik 'EXIT' untuk keluar) : "))
    if jumlahAkun == 5:
        print("Jumlah Akun sudah mencapai 5, tidak bisa menambah akun lagi.")
        akun_input = str(input("Ketik 'EXIT' untuk keluar : "))
        while akun_input != "EXIT" and akun_input.lower() != "exit":
             akun_input = str(input("Batas akun sudah terpenuhi. Ketik 'EXIT' untuk keluar : "))
        else:
            print(f"Jumlah Akun yang terdaftar : {jumlahAkun}")
            break
else:
    print(f"Jumlah Akun yang terdaftar : {jumlahAkun}")

for i in range(jumlahAkun):
    print(f"Akun ke-{i+1} : {akun[i]}")
else:
    print("Semua akun sudah ditampilkan.")
