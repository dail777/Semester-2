topi_list = [1, 2, 3, 4, 5]
tengah = len(topi_list) // 2 #menghitung indeks tengah dengan membagi panjang list dengan 2 menggunakan operator floor division

angka = int(input("Masukkan angka: ")) #meminta input angka dari pengguna dan mengkonversinya menjadi tipe data integer
topi_list.insert(tengah, angka) #menambahkan angka ke dalam list topi_list pada indeks tengah menggunakan fungsi insert()

topi_list.pop() #menghapus elemen terakhir dari list topi_list menggunakan fungsi pop()
print("Panjang List : ", len(topi_list)) #menghitung panjang list topi_list menggunakan

print(topi_list)