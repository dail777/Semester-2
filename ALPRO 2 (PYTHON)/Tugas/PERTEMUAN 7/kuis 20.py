exo = []

exo.append("Suho")
exo.append("Kai")
exo.append("Chanyeol")
exo.append("Sehun")

print(f"Anggota EXO: {exo}")

anggota_tambahan = ["DO", "Baekhyun", "Kris", "Lay", "Luhan", "Tao", "Chen"]
for anggota in anggota_tambahan:
    exo.append(anggota)
print(f"Anggota EXO Setelah Ditambah: {exo}")

exo.remove("Kris")
exo.remove("Luhan")
exo.remove("Tao")
print(f"Anggota EXO Setelah Dihapus: {exo}")

exo.insert(len(exo) - 2, "Xiumin")

print(exo)
