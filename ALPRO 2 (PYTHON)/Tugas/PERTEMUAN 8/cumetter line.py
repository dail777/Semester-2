import os
#dail
#garis sepanjang 60 karakter sebagai pembatas
def garis20():
    print("=" * 60)

#untuk membersihkan layar dan membuat tampilan lebih rapih
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

alert = None
uang = 0
member = False

users = {}
user_data = {}
current_user = None

# alert system
def set_alert(pesan):
    global alert
    alert = pesan


def show_alert():
    global alert
    if alert:
        print(f"{alert}")
        garis20()
        alert = None


def sync_data():
    global current_user, uang, member
    if current_user:
        user_data[current_user]["uang"] = uang
        user_data[current_user]["member"] = member


#sistem top up dan member
#wawan
def top_up(saldo_saat_ini):
    try:
        jumlah = int(input("Masukkan jumlah top up: "))
        set_alert(f"✅ Top up berhasil! Saldo {jumlah} telah ditambahkan.")
        hasil = saldo_saat_ini + jumlah
        sync_data()
        return hasil
    except:
        set_alert("⚠️ Input top up tidak valid!")
        return saldo_saat_ini


def pilih_member():
    global uang, member
    clear()

    harga_member = 20000
    garis20()
    print("Beli member")
    print("1. Ya")
    print("2. Tidak")
    garis20()

    opsi = input("Pilih (1-2): ")

    if opsi != "1":
        set_alert("⚠️ Pembelian dibatalkan.")
        return

    if uang >= harga_member:
        uang -= harga_member
        member = True
        set_alert(f"✅ Berhasil join member! Sisa saldo: {uang}")
        sync_data()
    else:
        set_alert(f"⚠️ Saldo tidak cukup. Harga: {harga_member}, Saldo: {uang}")


def menu_top_up():
    global uang

    while True:
        clear()
        garis20()
        print("MENU SALDO")
        garis20()
        print(f"SALDO  : {uang}")
        print(f"MEMBER : {'Aktif' if member else 'Tidak Aktif'}")
        print("1. Isi Saldo")
        print("2. Join Member")
        print("3. Kembali")
        garis20()
        show_alert()

        pilih = input("Pilih menu: ")

        if pilih == "1":
            uang = top_up(uang)
            sync_data()
        elif pilih == "2":
            pilih_member()
        elif pilih == "3":
            return
        else:
            set_alert("⚠️ Menu tidak valid!")


#penampilan stasiun dan pemilihan rute
#dail
stasiun = [
    "Jakarta Kota", "Tanggerang", "Bogor", "Bekasi", "Duri",
    "Rangkasbitung", "Cikarang", "Depok", "Serpong", "Cilebut"
] #list stasiun


def tampilStasiun(): #menampilkan daftar stasiun
    garis20()
    print("DAFTAR STASIUN")
    garis20()
    for i in range(len(stasiun)):
        print(f"{i + 1}. {stasiun[i]}")
    garis20()


def penampilStasiun(): #menampilkan daftar stasiun sekaligus dapat memilih rute
    while True:
        clear()
        tampilStasiun()
        print("1. Kembali")
        print("2. Pilih Rute")
        garis20()
        show_alert()

        inputan = input("Pilih Nomor : ")

        if inputan == "1":
            return
        elif inputan == "2":
            pilihRute()
        else:
            set_alert("⚠️ Menu tidak valid!")


def pilihRute(): #memilih rute dan menghitung harga berdasarkan jarak stasiun
    global uang

    clear()
    tampilStasiun()

    stasiunAwal = input("Dari : ").strip()
    stasiunTujuan = input("Ke   : ").strip()

    stasiun_lower = [s.lower() for s in stasiun]

    if stasiunAwal.lower() not in stasiun_lower or stasiunTujuan.lower() not in stasiun_lower:
        set_alert("⚠️ Stasiun tidak valid!")
        return

    indexAwal = stasiun_lower.index(stasiunAwal.lower())
    indexTujuan = stasiun_lower.index(stasiunTujuan.lower())

    jarak = abs(indexTujuan - indexAwal) #menghitung jarak stasiun dan mempositifkan jika hasilnya negatif
    hargaPerStasiun = 5000

    if member:
        hargaPerStasiun *= 0.7 #diskon 30% untuk member

    harga = int(jarak * hargaPerStasiun)

    clear()
    garis20()
    print(f"Rute   : {stasiun[indexAwal]} -> {stasiun[indexTujuan]}")
    print(f"Jarak  : {jarak} stasiun")
    print(f"Harga  : Rp {harga}")
    if member:
        print("Selamat! Anda mendapatkan diskon 30% karena anda member!")
    else:
        print("Jadi member dan dapatkan diskon 30% untuk setiap perjalanan!")
    garis20()

    confirm = input('Ketik "KONFIRMASI" atau "BATAL": ').upper()

    if confirm == "KONFIRMASI":
        if uang >= harga:
            uang -= harga
            set_alert(f"✅ Rute berhasil dipilih! Sisa saldo: {uang}")
            sync_data()
        else:
            set_alert("⚠️ Saldo tidak cukup!")
    elif confirm == "BATAL":
        set_alert("⚠️ Pembelian dibatalkan.")
    else:
        set_alert("⚠️ Input tidak valid!")


#menu utama
#lasiah

def register():
    clear()
    garis20()
    print("REGISTER COMMUTER LINE")
    garis20()
    show_alert()

    username = input("Masukkan username: ")

    if username in users:
        set_alert("Username sudah terdaftar!")
        return

    password = input("Masukkan password: ")
    users[username] = password
    user_data[username] = {"uang": 0, "member": False}
    set_alert("✅ Registrasi berhasil!")


def login():
    clear()
    garis20()
    print("LOGIN COMMUTER LINE")
    garis20()
    show_alert()

    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in users and users[username] == password:
        global current_user, uang, member
        current_user = username
        uang = user_data[username]["uang"]
        member = user_data[username]["member"]
        set_alert("✅ Login berhasil!")
        menu_commuter()
    else:
        set_alert("⚠️ Username atau password salah!")


def menu_commuter():
    while True:
        clear()
        garis20()
        print("MENU COMMUTER LINE")
        garis20()
        print(f"SALDO  : {uang}")
        print(f"MEMBER : {'Aktif' if member else 'Tidak Aktif'}")
        print("1. Daftar Stasiun")
        print("2. Pilih Rute")
        print("3. Isi Saldo / Member")
        print("4. Logout")
        garis20()
        show_alert()

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            penampilStasiun()
        elif pilihan == "2":
            pilihRute()
        elif pilihan == "3":
            menu_top_up()
        elif pilihan == "4":
            set_alert("✅ Logout berhasil!")
            break
        else:
            set_alert("⚠️ Pilihan tidak valid!")


while True:
    clear()
    garis20()
    print("SISTEM COMMUTER LINE")
    garis20()
    print("1. Register")
    print("2. Login")
    print("3. Keluar")
    garis20()
    show_alert()

    pilih = input("Pilih menu: ")

    if pilih == "1":
        register()
    elif pilih == "2":
        login()
    elif pilih == "3":
        clear()
        print("Terima kasih! Senang Melayani Anda!")
        break
    else:
        set_alert("⚠️ Pilihan tidak valid!")