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

