bilangan = [x for x in range(1, 11)]
bilangan_genap = [x for x in bilangan if x % 2 == 0]
bilangan_genap_kali_3 = [x * 3 for x in bilangan_genap]

print(bilangan)
print("Bilangan genap 1-10:", bilangan_genap)
print("Bilangan genap 1-10 dikali 3:", bilangan_genap_kali_3)