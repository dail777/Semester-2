secret_number = 777

text1 = "Selamat datang di game saya muggle!"
text2 = "masukkan suatu angka dan tebak"
text3 = "angka berapa yang saya pilih"
text4 = "untuk kamu."
text5 = "Jadi, berapa angka rahasianya?"


print("+" + "=" * 42 + "+")
print(f"| {text1.ljust(40)} |")
print(f"| {text2.ljust(40)} |")
print(f"| {text3.ljust(40)} |")
print(f"| {text4.ljust(40)} |")
print(f"| {text5.ljust(40)} |")
print("+"+"=" * 42 + "+")


angka_tebakan = int(input("Masukan angka tebakan : "))
while angka_tebakan != secret_number:
    print("hahaha! kamu nyangkut deh di Loop saya")
    angka_tebakan = int(input("Masukan angka tebakan : "))
else :
    print("Selamat, Muggle! kamu bebas sekarang!")