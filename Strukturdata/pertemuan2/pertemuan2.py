# Membuat List
import sys
logs: list[int] =[9]
print(logs)
print(sys.getsizeof(logs)) # ukuran list

# Menambahkan element di dalam list logs
logs.append(1)
print(logs)
print(sys.getsizeof(logs)) # ukuran list setelah penambahan element

# Menambahkan element di dalam list logs ke tiga
logs.append(2)
print(logs)
print(sys.getsizeof(logs)) # ukuran list setelah penambahan element ke tiga

# Menambahkan element di dalam list logs ke empat
logs.append(3)
print(logs)
print(sys.getsizeof(logs)) # ukuran list setelah penambahan element ke empat

# Menambahkan element di dalam list logs di depan ke lima
logs.insert(0, 5)
print(logs)
print(sys.getsizeof(logs)) # ukuran list setelah penambahan element ke lima

#menghapus element di dalam list logs
logs.pop(2)
print(logs)
print(sys.getsizeof(logs)) # ukuran list setelah penghapusan element ke tiga

#sort list logs
logs.sort(reverse= True )
print(logs)
#mencari jumlah di dalam list logs
print(sum(logs))
print(sys.getsizeof(logs)) # ukuran list setelah penjumlahan element di dalam list logs

print(len(logs)) # jumlah element di dalam list logs
print(sys.getsizeof(logs)) # ukuran list setelah menghitung jumlah element di dalam list logs

logs_backup : list[int] = logs.copy() # membuat backup list logs

print(logs_backup) # menampilkan backup list logs