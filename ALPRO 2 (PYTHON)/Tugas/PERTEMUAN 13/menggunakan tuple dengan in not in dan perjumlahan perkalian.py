tuple1 = (1, 2, 3, 4, 5)
total = 0
for i in range(len(tuple1)):
    total = total + tuple1[i] * 2
print("Total:", total)


if 10 not in tuple1:
    print("10 tidak ada di dalam tuple")

if 3 in tuple1:
    print("3 ada di dalam tuple")
