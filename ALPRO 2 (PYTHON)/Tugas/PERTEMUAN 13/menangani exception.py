data = {
    "nama": "Budi",
    "umur": 20
}

try:
    print(data["alamat"])
except KeyError:
    print("Key tidak ditemukan")