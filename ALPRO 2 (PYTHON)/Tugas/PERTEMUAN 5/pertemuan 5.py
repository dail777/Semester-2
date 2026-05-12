# ========================================================
# Comparasion Decision.py
# ========================================================
x = 1
y = 0

print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)


# ========================================================
# fungsi max.py
# ========================================================
x = int(input("Masukan nilai x:"))
y = int(input("Masukan nilai y:"))
z = int(input("Masukan nilai z:"))

print("Nilai x: ", x)
print("Nilai y: ", y)
print("Nilai z: ", z)

paling_besar = max(x, y, z)
print("Nilai paling besar yaitu: ", paling_besar)


# ========================================================
# if-elif-else.py
# ========================================================
while True:
    x = int(input("Masukan angka 1-10 :"))
    if x < 0:
        print("Masukan angka > 0")
    elif x >= 0 and x <= 10:
        print("Angka anda : ", x)
    else:
        print("Masukan angka 1 - 10")
    break


# ========================================================
# iftunggal.py
# ========================================================
n = int(input("Masukan nilai n: "))
if n == 10:
    print("Nilai n adalah 10")


# ========================================================
# kuis 11.py
# ========================================================
n = input("Masuka nilai n: ")
int_n = int(n)
if int_n >= 100:
    print("True")
else:
    print("False")


# ========================================================
# kuis 12.py
# ========================================================
x = int(input("Masukan nilai x:"))
y = int(input("Masukan nilai y:"))
z = int(input("Masukan nilai z:"))

if x > y and x > z :
    paling_besar = x
    print(f"Nilai paling besar yaitu x dengan nilai {paling_besar}")
elif y > x and y > z :
    paling_besar = y
    print(f"Nilai paling besar yaitu y dengan nilai {paling_besar}")
elif z > x and z > y :
    paling_besar = z
    print(f"Nilai paling besar yaitu z dengan nilai {paling_besar}")
else :
    print("Nilai x, y, atau z sama besar")


# ========================================================
# membandingkan.py
# ========================================================
x = int(input("Masukan nilai x:"))
y = int(input("Masukan nilai y:"))

if x > y :
    paling_kecil = y
    print(f"Nilai {paling_kecil} lebih kecil dari {x}")
elif x == y :
    print(f"Nilai {x} sama dengan {y}")
else :
    paling_kecil = x
    print(f"Nilai {paling_kecil} lebih kecil dari {y}")


# ========================================================
# menghitung pajak.py
# ========================================================
pendapatan = int(input("Masukan pendapatan anda: "))
tax = 0

if pendapatan <= 60000000:
    tax = 5 / 100 * pendapatan
elif pendapatan > 60000000 and pendapatan <= 250000000:
    tax = 15 / 100 * pendapatan
elif pendapatan > 250000000 and pendapatan <= 500000000:
    tax = 25 / 100 * pendapatan
elif pendapatan > 500000000 :
    tax = 30 / 100 * pendapatan

print(f"Pajak yang harus dibayar adalah {tax} rupiah")


# ========================================================
# rangkaian if.py
# ========================================================
n = int(input("Masukan nilai n: "))
if n < 10:
    print("Nilai n kurang dari 10")
if n > 10:
    print("Nilai n lebih dari 10")
if n == 10:
    print("Nilai n adalah 10")


# ========================================================
# statement decision.py
# ========================================================
m = input("Masukan nilai m:")
int_m = int(m)
if int_m < 100:
    print("Nilai kamu kurang dari 100")
else:
    print("Nilai kamu tidak kurang dari 100")
