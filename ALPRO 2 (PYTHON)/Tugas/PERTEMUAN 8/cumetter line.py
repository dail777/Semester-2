
def garis20():
    for i in range(20):
        print("=", end="")
    print()
uang = 0
member = False # Ganti nama agar tidak bentrok dengan nama fungsi

def top_up(saldo_saat_ini):
    jumlah = int(input("Masukkan jumlah top up: "))
    return saldo_saat_ini + jumlah

def pilih_member():
    global uang, member # Ambil akses ke variabel global
    
    harga_member = 0
    print("\nBeli member\n 1. ya \n 2. tidak")
    opsi = int(input("Pilih (1-3): "))
    
    if opsi == 1:
        harga_member = 20000
    else:
        print("Pilihan tidak tersedia.")
        return

    # Cek apakah uang cukup untuk beli member
    if uang >= harga_member:
        uang -= harga_member
        member = True
        print(f"Berhasil join! Sisa saldo: {uang}")
    else:
        print(f"Saldo tidak cukup. Harga member: {harga_member}, Saldo kamu: {uang}")

def menu_top_up():
    global uang # WAJIB agar bisa update nilai uang di baris 42
    global menu_top_up
    print(f"""
    ===================
    SALDO : {uang}
    MEMBER: {"Aktif" if member else "Tidak Aktif"}
    ===================
    1. Isi Saldo
    2. Join Member
    """)

    pilih = int(input("Pilih menu: "))

    if pilih == 1:
        uang = top_up(uang) # Update saldo global
        menu_commuter()      # Panggil lagi biar menu terupdate
    elif pilih == 2:
        pilih_member()
        menu_commuter()
    else:
        print("Menu tidak valid.")


#rute - kalo member = diskon
stasiun = ["Jakarta Kota", "Tanggerang", "Bogor", "Bekasi", "Duri", "Rangkasbitung", "Cikarang", "Depok", "Serpong", "Cilebut"]
hargaPerStasiun = 0
def tampilStasiun():
    print("Daftar stasiun: ")
    for i in range(len(stasiun)):
        print(f"{i+1}. {stasiun[i]}")
        
def pilihRute():
    garis20()
    tampilStasiun()
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



#dail

#login / register
#lasiah
# Database sederhana (menyimpan user)
users = {}

# Fungsi register
def register():
    print("\n=== REGISTER COMMUTER LINE ===")
    username = input("Masukkan username: ")
    
    if username in users:
        print("Username sudah terdaftar!")
        return
    
    password = input("Masukkan password: ")
    users[username] = password
    print("Registrasi berhasil!")

# Fungsi login
def login():
    print("\n=== LOGIN COMMUTER LINE ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    if username in users and users[username] == password:
        print("Login berhasil! Selamat datang di Commuter Line 🚆")
        menu_commuter()
    else:
        print("Username atau password salah!")

# Menu setelah login
def menu_commuter():
    while True:
        print(f"\nsaldo : {uang}")
        print(f"MEMBER :{"Aktif" if member else "Tidak Aktif"}")
        print("=== MENU COMMUTER LINE ===")
        print("1. daftar stasiun")
        print("2. pilih rute")
        print("3. isi saldo / join member")
        print("4. Logout")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            tampilStasiun()
        elif pilihan == "2":
            pilihRute()
        elif pilihan == "3":
            menu_top_up()
        elif pilihan == "4":
            print("Logout berhasil!")
            break
        else:
            print("Pilihan tidak valid!")

# Program utama
while True:
    print("\n=== SISTEM COMMUTER LINE ===")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")
    
    pilih = input("Pilih menu: ")
    
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

# Jalankan program



