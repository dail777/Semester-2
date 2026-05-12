def hitung_imt(berat, tinggi):
    tinggi = tinggi / 100
    imt = berat / (tinggi ** 2)
    return imt

berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (cm): "))

index_massa_tubuh = hitung_imt(berat, tinggi)
kategori = ["Normal", "Gemuk", "Obesitas"]

if index_massa_tubuh < 25:
    print("IMT anda adalah :", index_massa_tubuh, "termasuk kategori", kategori[0])
elif index_massa_tubuh < 30:
    print("IMT anda adalah :", index_massa_tubuh, "termasuk kategori", kategori[1])
else:
    print("IMT anda adalah :", index_massa_tubuh, "termasuk kategori", kategori[2])