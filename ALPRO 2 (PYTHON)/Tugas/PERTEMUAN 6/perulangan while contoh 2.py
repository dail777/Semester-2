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