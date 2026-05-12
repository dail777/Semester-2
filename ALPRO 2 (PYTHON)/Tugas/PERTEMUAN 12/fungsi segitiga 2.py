def cek_segitiga(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True

print(cek_segitiga(1, 1, 1))
print(cek_segitiga(1, 2, 3))
    