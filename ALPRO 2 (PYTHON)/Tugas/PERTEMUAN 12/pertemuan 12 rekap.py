#variable di dalam fungsi
def kuadrat(bilangan):
    hasil = bilangan ** 2
    return hasil

print(kuadrat(5))

#variable diluar fungsi 
bilangan = 10

def kuadrat():
    hasil = bilangan ** 2
    return hasil

print(kuadrat())

#variable diluar fungsi 2
def perkalian(x):
    pengkali = 5
    hasil = pengkali * x
    return hasil

pengkali = 10
print(perkalian(5))

#variable global
bilangan = 2
print(bilangan)

def kuadrat():
    global bilangan
    bilangan = 5 
    hasil = bilangan ** 2
    return hasil

print(kuadrat())
print(bilangan)

#kuis imt
def hitung_imt(berat, tinggi):
    tinggi = tinggi / 100
    imt = berat / (tinggi ** 2)
    return imt

berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (cm): "))

index_massa_tubuh = hitung_imt(berat, tinggi)
kategori = ["Normal", "Gemuk", "Obesitas"]

if index_massa_tubuh < 25:
    print("IMT anda adalah :", index_massa_tubuh, "termasuk kategori", kategori[0])
elif index_massa_tubuh < 30:
    print("IMT anda adalah :", index_massa_tubuh, "termasuk kategori", kategori[1])
else:
    print("IMT anda adalah :", index_massa_tubuh, "termasuk kategori", kategori[2])

#fungsi segitiga 1
def cek_segitiga(a, b, c):
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if b + c <= a:
        return False
    return True

print(cek_segitiga(1, 1, 1))
print(cek_segitiga(1, 2, 3))
    
#fungsi segitiga 2
def cek_segitiga(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True

print(cek_segitiga(1, 1, 1))
print(cek_segitiga(1, 2, 3))
    

#fungsi segitiga 3
def cek_segitiga(a, b, c):
    return a + b > c and a + c > b and b + c > a

print(cek_segitiga(1, 1, 1))
print(cek_segitiga(1, 2, 3))
    
#kuis faktorial
def faktorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil    

n = int(input("masukkan nilai yang ingin di faktorialkan: "))
print(n, "! = ", faktorial(n))

#kuis fibonacci
def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    

    elm_1 = elm_2 = 1
    hasil_jumlah = 0 
    for i in range(3, n + 1):
        hasil_jumlah = elm_1 + elm_2
        elm_1, elm_2 = elm_2, hasil_jumlah

    return hasil_jumlah

#test
for i in range(1, 10):
    print(i, "->", fibonacci(i))


#rekursif faktorial
def faktorial(n):
    if n < 0:
        return None
    if n < 3:
        return 1
    return n * faktorial(n - 1)

n = int(input("masukkan nilai yang ingin di faktorialkan: "))
print(n, "! = ", faktorial(n))

#rekursif fibonacci
def fibonacci(n):
    if n < 0:
        return None
    if n < 3:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

#test
for i in range(1, 11):
    print(i, "->", fibonacci(i))
