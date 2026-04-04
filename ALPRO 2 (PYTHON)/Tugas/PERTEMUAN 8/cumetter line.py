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
        print("\n=== MENU COMMUTER LINE ===")
        print("1. Lihat Rute")
        print("2. Pesan Tiket")
        print("3. Logout")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            print("Rute tersedia: Jakarta - Bogor, Jakarta - Bekasi, Jakarta - Cikarang")
        elif pilihan == "2":
            tujuan = input("Masukkan tujuan: ")
            print(f"Tiket ke {tujuan} berhasil dipesan!")
        elif pilihan == "3":
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
uang = 0
is_member = False # Ganti nama agar tidak bentrok dengan nama fungsi

def top_up(saldo_saat_ini):
    jumlah = int(input("Masukkan jumlah top up: "))
    return saldo_saat_ini + jumlah

def pilih_member():
    global uang, is_member # Ambil akses ke variabel global
    
    harga_member = 0
    print("\nPilih Member:\n1. Bronze (20rb)\n2. Silver (30rb)\n3. Gold (50rb)")
    opsi = int(input("Pilih (1-3): "))
    
    if opsi == 1:
        harga_member = 20000
    elif opsi == 2:
        harga_member = 30000
    elif opsi == 3:
        harga_member = 50000
    else:
        print("Pilihan tidak tersedia.")
        return

    # Cek apakah uang cukup untuk beli member
    if uang >= harga_member:
        uang -= harga_member
        is_member = True
        print(f"Berhasil join! Sisa saldo: {uang}")
    else:
        print(f"Saldo tidak cukup. Harga member: {harga_member}, Saldo kamu: {uang}")

def menu_top_up():
    global uang # WAJIB agar bisa update nilai uang di baris 42
    
    print(f"""
    ===================
    SALDO : {uang}
    MEMBER: {"Aktif" if is_member else "Tidak Aktif"}
    ===================
    1. Isi Saldo
    2. Join Member
    """)

    pilih = int(input("Pilih menu: "))

    if pilih == 1:
        uang = top_up(uang) # Update saldo global
        menu_top_up()       # Panggil lagi biar menu terupdate
    elif pilih == 2:
        pilih_member()
        menu_top_up()
    else:
        print("Menu tidak valid.")

# Jalankan program
menu_top_up()


#rute - kalo member = diskon
rute = ["jakarta", "bandung", "surabaya", "yogyakarta"]
print("Rute yang tersedia:")
for i, r in enumerate(rute):
    print(f"{i + 1}. {r}")
pilihan = int(input("Pilih rute (1-4): "))
if 1 <= pilihan <= len(rute):
    print(f"Anda memilih rute: {rute[pilihan - 1]}")
else:    
    print("Pilihan tidak valid.")
