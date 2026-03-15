power = 1
angka = int(input("Masukan Angka Untuk Melihat Perpangkatan 0-10: "))
for expo in range(11):
    print(f"{angka} pangkat {expo} adalah {power}")
    power *= angka