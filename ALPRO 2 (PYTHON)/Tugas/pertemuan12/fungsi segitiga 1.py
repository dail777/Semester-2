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
    