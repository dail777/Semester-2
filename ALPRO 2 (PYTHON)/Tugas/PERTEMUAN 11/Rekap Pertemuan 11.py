#return tanpa expresi
def berhitung(selesai = False):
    print(1)
    print(2)
    print(3)
    print(4)
    print(5)
    if not selesai:
        return
    print("perhitungan selesai")

berhitung()

#return tanpa ekspresi 2
def selamat_ulang_tahun(harapan = True):
    print("Tiga...")
    print("Dua...")
    print("Satu...")
    if not harapan:
        return
    print("Selamat Ulang Tahun")

selamat_ulang_tahun(False)
    
#return dengan ekspresi
def fungsiSemangat():
    print("Aku sangat semangat hari ini")
    return 100

x = fungsiSemangat()
print("Nilai untuk hari ini :", x)


#return dengan ekspresi mengabaikan return
def fungsiSemangat():
    print("Aku sangat semangat hari ini")
    return 100

fungsiSemangat()
print("Tapi Boong")
print("Aku sangat malas hari ini")

#keyword none
def weirdFunction(angka):
    if angka % 2 == 0:
        return True

print(weirdFunction(2))
print(weirdFunction(3))

#list sebagai parameter
def perjumlahanList(list):
    hasil = 0

    for elemen in list:
        hasil += elemen

    return hasil

print(perjumlahanList([8, 2 , 3]))

#Ganti argumen
def perjumlahanList(list):
    hasil = 0

    for elemen in list:
        hasil += elemen

    return hasil

print(perjumlahanList(7))

#list dari hasil fungsi
def penghasilList(panjang):
    listKosong = []

    for i in range(0, panjang):
        listKosong.append(i)

    return listKosong

print(penghasilList(8))

#kuis 23
def tahun_kabisat(tahun):
    if tahun % 400 == 0:
        return True
    elif tahun % 100 == 0:
        return False
    elif tahun % 4 == 0:
        return True
    else:
        return False

data_uji = [1900, 2000, 2016, 1987]
data_hasil = [False, True, True, False]

for i in range(len(data_uji)):
    th = data_uji[i]
    print(th, "->", end="")
    hasil = tahun_kabisat(th)
    if hasil == data_hasil[i]:
        print("OK")
    else:
        print("Gagal")

#kuis 24
def tahun_kabisat(tahun):
    if tahun % 400 == 0:
        return True
    elif tahun % 100 == 0:
        return False
    elif tahun % 4 == 0:
        return True
    else:
        return False

def hari_didalam_bulan(tahun, bulan):
    if bulan == 2:
        if tahun_kabisat(tahun):
            return 29
        else:
            return 28
    elif bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan in [4, 6, 9, 11]:
        return 30
    else:
        return None 

data_uji = [1900, 2000, 2016, 1987]
data_bulan = [2, 2, 1, 11]
data_hasil = [28, 29, 31, 30]

for i in range(len(data_uji)):
    th = data_uji[i]
    bln = data_bulan[i]
    print(th, bln, "->", end="")
    hasil = hari_didalam_bulan(th, bln)
    if hasil == data_hasil[i]:
        print("OK")
    else:
        print("Gagal")

#kuis 25
def tahun_kabisat(tahun):
    if tahun % 400 == 0:
        return True
    elif tahun % 100 == 0:
        return False
    elif tahun % 4 == 0:
        return True
    else:
        return False

def hari_didalam_bulan(tahun, bulan):
    if bulan == 2:
        if tahun_kabisat(tahun):
            return 29
        else:
            return 28
    elif bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan in [4, 6, 9, 11]:
        return 30
    else:
        return None 

def hari_pada_tahun(tahun, bulan, hari):
    if bulan < 1 or bulan > 12:
        return None
    jumlah_hari = hari_didalam_bulan(tahun, bulan)
    if jumlah_hari is None or hari < 1 or hari > jumlah_hari:
        return None
    total = 0
    for b in range(1, bulan):
        total += hari_didalam_bulan(tahun, b)
    return total + hari

data_uji = [1900, 2000, 2016, 1987]
data_bulan = [2, 2, 1, 11]
data_hari = [28, 29, 31, 30]
data_hasil = [59, 60, 31, 334]

for i in range(len(data_uji)):
    th = data_uji[i]
    bln = data_bulan[i]
    hr = data_hari[i]
    hasil = hari_pada_tahun(th, bln, hr)
    print(th, bln, hr, hasil, "->", end="")
    if hasil == data_hasil[i]:
        print("Ok")
    else:
        print("Gagal")

print(hari_pada_tahun(2000, 12, 31))

#kuis 26
def cek_prima(bilangan):
    if bilangan <= 1:
        return False
    for i in range(2, bilangan):
        if bilangan % i == 0:
            return False
    return True

for i in range(1, 20):
    if cek_prima(i + 1):
        print(i + 1, end=" ")
print()

#kuis 27
def cek_prima(bilangan):
    if bilangan <= 1:
        return False
    for i in range(2, bilangan):
        if bilangan % i == 0:
            return False
    return True

for i in range(1, 20):
    if cek_prima(i + 1):
        print(i + 1, end=" ")
print()

#kuis 28
def liter100km_ke_mpg(liter):
    km_per_mil = 1.609344
    liter_per_galon = 3.785411784
    mil = 100 / km_per_mil
    galon = liter / liter_per_galon
    return mil / galon

def mpg_ke_liter100km(mil):
    km_per_mil = 1.609344
    liter_per_galon = 3.785411784
    km = mil * km_per_mil
    liter = liter_per_galon
    return (liter / km) * 100

print(liter100km_ke_mpg(3.9))
print(liter100km_ke_mpg(7.5))
print(liter100km_ke_mpg(10.))
print(mpg_ke_liter100km(60.3))
print(mpg_ke_liter100km(31.4))
print(mpg_ke_liter100km(23.5))