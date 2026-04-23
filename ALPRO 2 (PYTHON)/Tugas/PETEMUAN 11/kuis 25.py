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