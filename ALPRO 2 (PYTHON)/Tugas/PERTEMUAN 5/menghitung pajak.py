pendapatan = int(input("Masukan pendapatan anda: "))
tax = 0

if pendapatan <= 60000000:
    tax = 5 / 100 * pendapatan
elif pendapatan > 60000000 and pendapatan <= 250000000:
    tax = 15 / 100 * pendapatan
elif pendapatan > 250000000 and pendapatan <= 500000000:
    tax = 25 / 100 * pendapatan
elif pendapatan > 500000000 :
    tax = 30 / 100 * pendapatan

print(f"Pajak yang harus dibayar adalah {tax} rupiah")