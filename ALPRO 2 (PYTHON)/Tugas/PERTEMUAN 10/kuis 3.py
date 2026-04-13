data = [[2, 4], [6, 8], [10, 12]]

flatten = []
for angka in data:
    for isi in angka:
        flatten.append(isi)

print("Data:", data)
print("Data flatten:", flatten)
