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
rute = ["jakarta", "bandung", "surabaya", "yogyakarta"]
print("Rute yang tersedia:")
for i, r in enumerate(rute):
    print(f"{i + 1}. {r}")
pilihan = int(input("Pilih rute (1-4): "))
if 1 <= pilihan <= len(rute):
    print(f"Anda memilih rute: {rute[pilihan - 1]}")
else:    
    print("Pilihan tidak valid.")
