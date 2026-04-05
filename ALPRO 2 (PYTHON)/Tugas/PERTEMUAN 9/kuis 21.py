lotre = [3, 7, 11, 42, 34, 49]
lotreSudahKeluar = [5, 9, 11, 42, 3, 49]
tebakanBenar = 0

for angka in lotre:
    if angka in lotreSudahKeluar:
        tebakanBenar += 1

print(f"Jumlah tebakkan yang benar : {tebakanBenar}")