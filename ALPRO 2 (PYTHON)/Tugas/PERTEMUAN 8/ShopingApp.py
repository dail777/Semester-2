def garis20():
    for i in range(20):
        print("=", end="")
    print()
#dail
stasiun = ["Jakarta Kota", "Tanggerang", "Bogor", "Bekasi", "Duri", "Rangkasbitung", "Cikarang", "Depok", "Serpong", "Cilebut"]
hargaPerStasiun = 0
def pilihRute():
    garis20()
    print("Daftar stasiun: ")
    for i in range(len(stasiun)):
        print(f"{i+1}. {stasiun[i]}")
    stasiunAwal = str(input("Dari : "))
    stasiunTujuan = str(input("Ke : "))
    garis20()
    if member == False:
            hargaPerStasiun = 5000
            print("Jadi member dan dapatkan diskon 30% untuk setiap perjalanan!")
    if member == True:
            hargaPerStasiun = hargaPerStasiun * 30/100
            print("Selamat!Anda mendapatkan diskon 30% karena anda member!")
    if stasiunAwal in stasiun and stasiunTujuan in stasiun or stasiunAwal.upper() in stasiun and stasiunTujuan.upper() in stasiun or stasiunAwal.lower() in stasiun and stasiunTujuan.lower() in stasiun:
        indexAwal = stasiun.index(stasiunAwal)
        indexTujuan = stasiun.index(stasiunTujuan)
        jarak = abs(indexTujuan - indexAwal)
        harga = jarak * hargaPerStasiun
        print(f"Harga tiket dari {stasiunAwal} ke {stasiunTujuan} adalah Rp {harga}")
    else:
        print("Stasiun tidak valid!")
    garis20()
    confirm = input('Ketik "KONFIRMASI" untuk melanjutkan atau "BATAL" untuk membatalkan: ')
    if confirm.upper() == "KONFIRMASI" or confirm.lower() == "konfirmasi":
        print("Tiket berhasil dipesan!")
        uang = uang - harga
        print(f"Saldo anda tersisa : {uang}")
    elif confirm.upper() == "BATAL" or confirm.lower() == "batal":
        print("Pembelian tiket dibatalkan.")
        return pilihRute()
    
    pilihRute()