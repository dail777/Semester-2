#login / register
#lasiah
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
#dail

