data = {
    "nama": "Budi"
}

try:
    angka = int(input("Masukkan angka: "))
    print(10 / angka)
    print(data["umur"])

except ZeroDivisionError:
    print("Tidak boleh membagi dengan nol")

except ValueError:
    print("Input harus angka")

except KeyError:
    print("Key dictionary tidak ditemukan")