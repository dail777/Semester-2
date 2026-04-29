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