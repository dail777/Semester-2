def garis20():
    for i in range(20):
        print("=", end="")
    print()


#login / register
#lasiah
# database sederhana
users = {}

# REGISTER
def register():
    print("\n=== REGISTER ===")
    username = input("Username: ")
    
    if username in users:
        print("Username sudah ada!")
        return
    
    password = input("Password: ")
    users[username] = password
    print("Register berhasil!")

# LOGIN
def login():
    print("\n=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")
    
    if username in users and users[username] == password:
        print("Login berhasil!")
        menu(username)
    else:
        print("Login gagal!")

def menu(username):
    while True:
        print(f"\n=== MENU UTAMA ({username}) ===")
        print("1. Lihat Rute")
        print("2. Pesan Tiket")
        print("3. Top Up")
        print("4. Pembayaran")
        print("5. Logout")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            lihat_rute()      # fungsi teman
        elif pilihan == "2":
            pesan_tiket()     # fungsi teman
        elif pilihan == "3":
            top_up()          # fungsi teman
        elif pilihan == "4":
            pembayaran()      # fungsi teman
        elif pilihan == "5":
            print("Logout...")
            break
        else:
            print("Pilihan tidak valid!")

# PROGRAM UTAMA
while True:
    print("\n=== COMMUTER LINE ===")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")
    
    pilih = input("Pilih: ")
    
    if pilih == "1":
        register()
    elif pilih == "2":
        login()
    elif pilih == "3":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid!")
#topup - membeli member 
#wawan maulana
uang = 0
member = False
nyoba = true
def top_up(saldo_saat_ini):
    jumlah = int(input("Masukkan jumlah top up: "))
    return saldo_saat_ini + jumlah

def member():
    print("pilih member :\n 1. bronze\n 2. silver\n 3. gold")
    member = int(input("pilih member :"))
    if member == 1 :
        print("member bronze Rp : 20K")
    elif member == 2 :
        print("member silver Rp : 30K")
    elif member == 3 :
        print("member gold Rp : 50K")
    else :
        print("error")

#uang = top_up(uang)
#print(f"Saldo sekarang: {uang}")
member()



#rute - kalo member = diskon
stasiun = ["Jakarta Kota", "Tanggerang", "Bogor", "Bekasi", "Duri", "Rangkasbitung", "Cikarang", "Depok", "Serpong", "Cilebut"]
hargaPerStasiun = 0
def pilihRute():
    garis20()
    print("")
    stasiunAwal = str(input("Dari : "))
    stasiunTujuan = str(input("Ke : "))
    if member == False:
            hargaPerStasiun = 5000
            print("Jadi member dan dapatkan diskon 40% untuk setiap perjalanan!")
    if member == True:
            hargaPerStasiun = 3000
            print("Anda mendapatkan diskon 40% karena anda member!")
    if stasiunAwal in stasiun and stasiunTujuan in stasiun or stasiunAwal.upper() in stasiun and stasiunTujuan.upper() in stasiun or stasiunAwal.lower() in stasiun and stasiunTujuan.lower() in stasiun:
        indexAwal = stasiun.index(stasiunAwal)
        indexTujuan = stasiun.index(stasiunTujuan)
        jarak = abs(indexTujuan - indexAwal)
        harga = jarak * hargaPerStasiun
        print(f"Harga tiket dari {stasiunAwal} ke {stasiunTujuan} adalah Rp {harga}")
    else:
        print("Stasiun tidak valid!")
    confirm = input('Ketik "KONFIRMASI" untuk melanjutkan atau "BATAL" untuk membatalkan: ')
    if confirm.upper() == "KONFIRMASI" or confirm.lower() == "konfirmasi":
        print("Tiket berhasil dipesan!")
        uang = uang - harga
        print(f"Saldo anda tersisa : {uang}")
    elif confirm.upper() == "BATAL" or confirm.lower() == "batal":
        print("Pembelian tiket dibatalkan.")
        return pilihRute()



#dail


