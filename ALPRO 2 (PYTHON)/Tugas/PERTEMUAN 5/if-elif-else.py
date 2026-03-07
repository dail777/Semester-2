
while True:
    x = int(input("Masukan angka 1-10 :"))
    if x < 0:
        print("Masukan angka > 0")
    elif x >= 0 and x <= 10:
        print("Angka anda : ", x)
    else:
        print("Masukan angka 1 - 10")
    break