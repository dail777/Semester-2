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
<<<<<<< HEAD
rute = ["jakarta", "bandung", "surabaya", "yogyakarta"]
print("Rute yang tersedia:")
for i, r in enumerate(rute):
    print(f"{i + 1}. {r}")
pilihan = int(input("Pilih rute (1-4): "))
if 1 <= pilihan <= len(rute):
    print(f"Anda memilih rute: {rute[pilihan - 1]}")
else:    
    print("Pilihan tidak valid.")
=======
#dail

>>>>>>> 7bb32dd6a3fd60fc01304dc7293625a75c27ceec
