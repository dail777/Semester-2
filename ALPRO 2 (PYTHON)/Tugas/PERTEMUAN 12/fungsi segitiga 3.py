def cek_segitiga(a, b, c):
    return a + b > c and a + c > b and b + c > a

print(cek_segitiga(1, 1, 1))
print(cek_segitiga(1, 2, 3))
    