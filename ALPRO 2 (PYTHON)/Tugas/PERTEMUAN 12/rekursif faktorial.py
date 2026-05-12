def faktorial(n):
    if n < 0:
        return None
    if n < 3:
        return 1
    return n * faktorial(n - 1)

n = int(input("masukkan nilai yang ingin di faktorialkan: "))
print(n, "! = ", faktorial(n))