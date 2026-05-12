# ========================================================
# fungsi print float.py
# ========================================================
#Fungsi print dengan literal float
print(0.4)
print(4.0)

#Bentuk float tanpa angka 0 di depan (menggunakan notasi singkat)
print(.4)
print(4.)

#Float dengan notasi eksponensial
print(1.5e1)     # 15.0
print(2.5e-1)    # 0.25
print(3.0e+2)    # 300.0


# ========================================================
# fungsi print literal boolean.py
# ========================================================
print(True) #Fungsi print untuk mencetak nilai literal boolean True
print(False) #Fungsi print untuk mencetak nilai literal boolean False


# ========================================================
# kuis.py
# ========================================================
print((2 ** 4), (2 * 4.), (2 * 4))
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
print((2 % -4), (2 % 4), (2 ** 3 ** 2))


# ========================================================
# Literal dan Print.py
# ========================================================
nama = "Dail" #String Literal
umur = 20 #Int Literal
satuan = "cm" #String Literal
Tinggi = 175.6 #Float Literal

print("Nama:", nama) #Mencetak Text Nama: dan akan isi dari variable nama
print("Umur:", umur) #Mencetak Text Umur: dan akan isi dari variable umur
print("Tinggi:", Tinggi, satuan) #Mencetak Text Tinggi: dan akan isi dari variable Tinggi dan Satuan


# ========================================================
# operator modulo.py
# ========================================================
#Modulo (Hasil Bagi) Integer - Integer
print(10 % 3)
#Modulo (Hasil Bagi) Integer - Float
print(10 % 3.5)
#Modulo (Hasil Bagi) Float - Integer
print(10.5 % 3)
#Modulo (Hasil Bagi) Float - Float
print(10.5 % 3.5)


# ========================================================
# operator pembagian.py
# ========================================================
#Pembagian integer - integer
print(10 / 2)
#Pembagian integer - float
print(10 / 2.5)
#Pembagian float - integer
print(10.5 / 2)
#Pembagian float - float
print(10.5 / 2.5)


# ========================================================
# operator perkalian.py
# ========================================================
#Perkalian integer - integer
print(2 * 3)
#Perkalian integer - float
print(2 * 3.5)
#Perkalian float - integer
print(2.5 * 3)
#Perkalian float - float
print(2.5 * 3.5)


# ========================================================
# operator unary dan binary.py
# ========================================================
#Operator unary
print(-5) #Operator unary untuk negasi angka
print(+5) #Operator unary untuk menunjukkan angka positif
print(not True) #Operator unary untuk negasi boolean
print(not False) #Operator unary untuk negasi boolean

#Operator binary
print(2 + 3) #Operator binary untuk penjumlahan
print(5 - 2) #Operator binary untuk pengurangan
print(4 * 3) #Operator binary untuk perkalian
print(10 / 2) #Operator binary untuk pembagian
print(10 // 3) #Operator binary untuk pembagian integer
print(10 % 3) #Operator binary untuk modulo (sisa bagi)
print(2 ** 3) #Operator binary untuk pemangkatan


# ========================================================
# pembagian integer.py
# ========================================================
#Pembagian integer integer - integer
print(10 // 2)
#Pembagian integer integer - float
print(10 // 2.5)
#Pembagian integer float - integer
print(10.5 // 2)
#Pembagian integer float - float
print(10.5 // 2.5)


# ========================================================
# print integer.py
# ========================================================
angkaPositif = 11111111 #literal integer
angkaNegatif = -11111111 #literal integer
print("Angka Positif :", angkaPositif)
print("Angka Negatif :", angkaNegatif)


# ========================================================
# print pemangkatan.py
# ========================================================
#Pemangkatan integer-integer
print(2 ** 3)
#Pemangkatan integer-float
print(2 ** 3.5)
#Pemangkatan float-integer
print(2.5 ** 3)
#Pemangkatan float-float
print(2.5 ** 3.5)


# ========================================================
# print representasi bilangan octal dan hexadecimal.py
# ========================================================
    #Fungsi Representasi Octal 
def OctalRep(bilangan):
    bilangan = int(bilangan)
    print(f"{bilangan} dalam Octal = {oct(bilangan)}")
    print(f"Octal literal {oct(bilangan)} = {bilangan}")
   
    #Fungsi Representasi Hexadecimal
def HexadecimalRep(bilangan):
    bilangan = int(bilangan)
    print(f"{bilangan} dalam Hexadecimal = {hex(bilangan)}")
    print(f"Hexadecimal literal {hex(bilangan)} = {bilangan}")
    

    #Panggil fungsi
    OctalRep(15)
    HexadecimalRep(25)


# ========================================================
# print string petik 2 dan petik 1.py
# ========================================================
text = "String dengan Petik 2"
text2 = 'String dengan Petik 1'

print(text)
print(text2)


# ========================================================
# subekspresi.py
# ========================================================
#Fungsi Print Subekspresi
print(2 * (3 + 4)) #Fungsi print untuk mencetak hasil dari subekspresi 3 + 4 yang kemudian dikalikan dengan 2
print((10 - 5) / 2) #Fungsi print untuk mencetak hasil dari subekspresi 10 - 5 yang kemudian dibagi dengan 2
