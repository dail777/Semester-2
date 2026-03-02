jam = int(input("Waktu Mulai (jam) : "))
waktu = int(input("Waktu Mulai (menit) : "))
durasi = int(input("Durasi Acara (menit) : "))

total_menit = waktu + durasi
jam_selesai = jam + (total_menit // 60)
menit_selesai = total_menit % 60

print(f"Acara selesai pukul {jam_selesai}:{menit_selesai}")