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