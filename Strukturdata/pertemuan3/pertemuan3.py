import sys
LogApss = ("User 1 Login", "User 2 Login", "User 3 Login")
print(LogApss)
print(sys.getsizeof(LogApss))

#membuktikan memory tuple lebih efisien dari list
LogApssList = ["User 1 Login", "User 2 Login", "User 3 Login"]
print(LogApssList)
print(sys.getsizeof(LogApssList))

#pembuktian tuple tidak bisa diubah
#Tambah
# LogApss.append("User 4 Login")
#Ubah
# LogApss[0] = "User 1 Logout"
#hapus
# del LogApss[0]

#pembuktian tuple bisa diakses dengan index
for i in range(len(LogApss)):
    print(LogApss[i])

#menduplikat tuple
LogApssBackup = LogApss
print(LogApssBackup)
print(LogApss)