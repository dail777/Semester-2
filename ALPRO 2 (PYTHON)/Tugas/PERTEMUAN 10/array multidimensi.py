jadwal = [
    ["Matematika", "Informatika", "Sejarah", "Olahraga", "Bahasa Jepang"],
    ["Bahasa Indonesia", "Fisika", "Geografi", "Seni Budaya", "Bahasa Korea"],
]

hari = ["Senin", "Selasa"]

for i in range(2):  # hari
    print(hari[i] + " :")
    for j in range(5):  # mapel
        print("-", jadwal[i][j])
    print()