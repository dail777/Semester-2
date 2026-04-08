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