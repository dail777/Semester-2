#import library math untuk menggunakan fungsi sqrt
import math

# Menghitung sisi miring segitiga menggunakan rumus Pythagoras
# Input sisi-sisi segitiga
sisi_a = float(input("Masukkan panjang sisi a: "))
sisi_b = float(input("Masukkan panjang sisi b: "))

# Rumus Pythagoras: c² = a² + b²
hypo = math.sqrt(sisi_a**2 + sisi_b**2)

print(f"Sisi miring (hipotenusa) = {hypo}")