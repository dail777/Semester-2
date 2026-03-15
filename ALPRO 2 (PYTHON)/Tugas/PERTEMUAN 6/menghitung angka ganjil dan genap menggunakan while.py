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