# --- FUNGSI UTILITY ---
def garis20():
    print("=" * 20)

# --- DATA GLOBAL ---
uang = 0
is_member = False  # Menggunakan is_member agar tidak bentrok dengan nama fungsi/logika lain
stasiun = ["Jakarta Kota", "Tangerang", "Bogor", "Bekasi", "Duri", "Rangkasbitung", "Cikarang", "Depok", "Serpong", "Cilebut"]
users = {}

# --- SISTEM TOP UP & MEMBER ---
def top_up(saldo_saat_ini):
    try:
        jumlah = int(input("Masukkan jumlah top up: "))
        return saldo_saat_ini + jumlah
    except ValueError:
        print("Input harus angka!")
        return saldo_saat_ini

def pilih_member():
    global uang, is_member
    
    harga_member = 20000
    print(f"\nBeli member seharga Rp {harga_member}?")
    print("1. Ya\n2. Tidak")
    
    opsi = input("Pilih (1/2): ")
    
    if opsi == "1":
        if uang >= harga_member:
            uang -= harga_member
            is_member = True
            print(f"Berhasil join member! Sisa saldo: {uang}")
        else:
            print(f"Saldo tidak cukup. Harga member: {harga_member}, Saldo kamu: {uang}")
    else:
        print("Batal beli member.")

def menu_top_up():
    global uang
    print(f"""
    ===================
    SALDO : {uang}
    MEMBER: {"Aktif" if is_member else "Tidak Aktif"}
    ===================
    1. Isi Saldo
    2. Join Member
    3. Kembali
    """)

    pilih = input("Pilih menu: ")
    if pilih == "1":
        uang = top_up(uang)
    elif pilih == "2":
        pilih_member()
    elif pilih == "3":
        return

# --- SISTEM RUTE ---
def tampilStasiun():
    print("\nDaftar stasiun: ")
    for i, nama in enumerate(stasiun, 1):
        print(f"{i}. {nama}")
        
def pilihRute():
    global uang # WAJIB agar saldo berkurang saat konfirmasi
    garis20()
    tampilStasiun()
    
    # .title() digunakan agar input "bogor" otomatis jadi "Bogor" (sesuai list)
    awal = input("Dari : ").title()
    tujuan = input("Ke : ").title()
    
    if awal in stasiun and tujuan in stasiun:
        indexAwal = stasiun.index(awal)
        indexTujuan = stasiun.index(tujuan)
        jarak = abs(indexTujuan - indexAwal)
        
        if jarak == 0:
            print("Stasiun asal dan tujuan tidak boleh sama!")
            return

        # Logika Harga & Diskon
        harga_per_stasiun = 5000
        if is_member:
            # Diskon 30% berarti membayar 70% (0.7)
            harga_per_stasiun = int(harga_per_stasiun * 0.7)
            print("Selamat! Anda mendapatkan diskon 30% karena Anda member!")
        else:
            print("Tips: Jadi member untuk dapat diskon 30% setiap perjalanan.")

        total_harga = jarak * harga_per_stasiun
        print(f"Harga tiket dari {awal} ke {tujuan} adalah Rp {total_harga}")
        
        garis20()
        confirm = input('Ketik "KONFIRMASI" untuk membayar atau "BATAL": ').upper()
        
        if confirm == "KONFIRMASI":
            if uang >= total_harga:
                uang -= total_harga
                print(f"Tiket berhasil dipesan! Saldo anda tersisa : {uang}")
            else:
                print("Saldo tidak cukup! Silakan isi saldo terlebih dahulu.")
        else:
            print("Pemesanan dibatalkan.")
    else:
        print("Stasiun tidak valid! Pastikan ejaan benar.")

# --- SISTEM LOGIN & AUTH ---
def register():
    print("\n=== REGISTER COMMUTER LINE ===")
    username = input("Masukkan username: ")
    if username in users:
        print("Username sudah terdaftar!")
        return
    password = input("Masukkan password: ")
    users[username] = password
    print("Registrasi berhasil!")

def login():
    print("\n=== LOGIN COMMUTER LINE ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    if username in users and users[username] == password:
        print(f"Login berhasil! Selamat datang, {username} 🚆")
        menu_commuter()
    else:
        print("Username atau password salah!")

def menu_commuter():
    while True:
        print(f"\nSaldo : {uang} | MEMBER : {'Aktif' if is_member else 'Tidak Aktif'}")
        print("=== MENU COMMUTER LINE ===")
        print("1. Daftar Stasiun")
        print("2. Pilih Rute")
        print("3. Isi Saldo / Join Member")
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

# --- PROGRAM UTAMA ---
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