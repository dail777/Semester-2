# ============================================
# SISTEM MANAJEMEN AKADEMIK SEDERHANA
# Mata Kuliah : Algoritma & Pemrograman II
# Bahasa      : Python
# ============================================

# ---------- GLOBAL VARIABLE ----------
data_mahasiswa = []  # list of dictionary

# ---------- TUPLE (Bobot Nilai) ----------
BOBOT_NILAI = (0.3, 0.3, 0.4)  # tuple (immutable)

# ---------- FUNGSI VALIDASI INPUT ----------
def input_angka(prompt):
    """Validasi input numerik menggunakan exception"""
    while True:
        try:
            nilai = float(input(prompt))
            if nilai < 0 or nilai > 100:
                print("Nilai harus antara 0 - 100")
            else:
                return nilai
        except ValueError:
            print("Input harus berupa angka!")

# ---------- FUNGSI HITUNG NILAI ----------
def hitung_nilai(tugas, uts, uas):
    """Menghitung nilai akhir berdasarkan bobot"""
    return (tugas * BOBOT_NILAI[0]) + (uts * BOBOT_NILAI[1]) + (uas * BOBOT_NILAI[2])

# ---------- FUNGSI TENTUKAN GRADE ----------
def tentukan_grade(nilai_akhir):
    """Menentukan grade menggunakan conditional execution"""
    if nilai_akhir >= 85:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 55:
        return "C"
    else:
        return "D"

# ---------- FUNGSI INPUT DATA MAHASISWA ----------
def input_data_mahasiswa():
    """Input data mahasiswa dan menyimpannya ke list"""
    nim = input("Masukkan NIM        : ")
    nama = input("Masukkan Nama       : ")

    tugas = input_angka("Nilai Tugas (0-100) : ")
    uts   = input_angka("Nilai UTS (0-100)   : ")
    uas   = input_angka("Nilai UAS (0-100)   : ")

    # List multidimensi (nilai)
    nilai = [tugas, uts, uas]

    nilai_akhir = hitung_nilai(tugas, uts, uas)
    grade = tentukan_grade(nilai_akhir)

    # Operator bitwise (contoh status aktif)
    status_aktif = 1 & 1  # 1 = aktif

    mahasiswa = {
        "nim": nim,
        "nama": nama,
        "nilai": nilai,
        "nilai_akhir": nilai_akhir,
        "grade": grade,
        "status": status_aktif
    }

    data_mahasiswa.append(mahasiswa)
    print("\nData mahasiswa berhasil ditambahkan!\n")

# ---------- FUNGSI TAMPILKAN DATA ----------
def tampilkan_data():
    """Menampilkan seluruh data mahasiswa"""
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.\n")
        return

    print("\n===== DATA MAHASISWA =====")
    print("NIM\tNama\tNilai Akhir\tGrade")
    print("-" * 40)

    for mhs in data_mahasiswa:
        print(f"{mhs['nim']}\t{mhs['nama']}\t{mhs['nilai_akhir']:.2f}\t\t{mhs['grade']}")
    print()

# ---------- FUNGSI SORTING ----------
def sorting_data():
    """Mengurutkan data mahasiswa berdasarkan nilai akhir"""
    if not data_mahasiswa:
        print("Data kosong, tidak bisa sorting.\n")
        return

    data_mahasiswa.sort(key=lambda x: x["nilai_akhir"], reverse=True)
    print("Data berhasil diurutkan berdasarkan nilai akhir (DESC).\n")

# ---------- MENU UTAMA ----------
def menu():
    """Menu utama aplikasi"""
    while True:
        print("====================================")
        print(" SISTEM MANAJEMEN AKADEMIK PYTHON ")
        print("====================================")
        print("1. Input Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Sorting Data (Nilai Tertinggi)")
        print("4. Keluar")
        print("====================================")

        pilihan = input("Pilih menu (1-4): ")

        # Conditional execution & operator logika
        if pilihan == "1":
            input_data_mahasiswa()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            sorting_data()
        elif pilihan == "4":
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid!\n")

# ---------- PROGRAM UTAMA ----------
menu()
