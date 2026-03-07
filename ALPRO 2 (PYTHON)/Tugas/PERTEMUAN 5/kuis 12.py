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