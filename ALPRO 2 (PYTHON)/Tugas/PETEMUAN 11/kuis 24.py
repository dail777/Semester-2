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