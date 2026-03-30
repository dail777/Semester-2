listNama = ["Andi", "Budi", "Citra", "Anto", "Devi"] #Membuat list kosong dengan nama listNama
print("List Awal:", listNama)
nama = str(input("Masukkan nama: "))
ruang = int(input("Masukkan Ruang Ke Berapa Yang Akan Diubah: "))
listNama[ruang-1] = nama #mengubah elemen pada ruang yang ditentukan dengan nama yang diinputkan 
print("List setelah ditambahkan nama:", listNama)


ruang = int(input("Masukkan Ruang Ke Berapa Yang Akan Dicopy: "))
ruang2 = int(input("Masukkan Ruang Ke Berapa Yang Akan Diisi: "))
listNama[ruang2-1] = listNama[ruang-1] #Menambahkan nama ke dalam listNama
print(f"Ruang Ke-{ruang} telah dicopy ke Ruang Ke-{ruang2}")
print("List setelah dikopi:", listNama)
