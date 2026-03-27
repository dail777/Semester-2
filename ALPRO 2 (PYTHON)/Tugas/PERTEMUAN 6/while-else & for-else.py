jumlahAkun = 0
akun : list = []

akun_input = str(input("Masukan Nama Akun Batas 5 Akun Untuk diinput (Ketik 'EXIT' untuk keluar) : "))
while akun_input != "EXIT" and akun_input.lower() != "exit":
    if akun_input == "EXIT" or akun_input.lower() == "exit":
        break
    akun.append(akun_input)
    jumlahAkun += 1
    akun_input = str(input("Masukan Nama Akun Batas 5 Akun Untuk diinput (Ketik 'EXIT' untuk keluar) : "))
    if jumlahAkun == 5:
        print("Jumlah Akun sudah mencapai 5, tidak bisa menambah akun lagi.")
        akun_input = str(input("Ketik 'EXIT' untuk keluar : "))
        while akun_input != "EXIT" and akun_input.lower() != "exit":
             akun_input = str(input("Batas akun sudah terpenuhi. Ketik 'EXIT' untuk keluar : "))
        else:
            print(f"Jumlah Akun yang terdaftar : {jumlahAkun}")
            break
else:
    print(f"Jumlah Akun yang terdaftar : {jumlahAkun}")

for i in range(jumlahAkun):
    print(f"Akun ke-{i+1} : {akun[i]}") 
else:
    print("Semua akun sudah ditampilkan.")