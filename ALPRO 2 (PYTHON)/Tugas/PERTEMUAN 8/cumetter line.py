#login / register
#topup - membeli member 
uang = 0
member = False

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
