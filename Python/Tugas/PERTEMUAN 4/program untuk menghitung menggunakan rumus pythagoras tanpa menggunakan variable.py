#import library math untuk menggunakan fungsi sqrt
import math

# Menghitung sisi miring segitiga menggunakan rumus Pythagoras
# Input sisi-sisi segitiga
sisi_a = float(input("Masukkan panjang sisi a: "))
sisi_b = float(input("Masukkan panjang sisi b: "))

print("Sisi miring (hipotenusa) :", math.sqrt(sisi_a**2 + sisi_b**2))