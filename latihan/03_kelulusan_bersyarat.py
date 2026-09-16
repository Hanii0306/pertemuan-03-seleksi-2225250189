# 03_kelulusan_bersyarat.py

nilai = float(input("Masukkan nilai akhir: "))
kehadiran = float(input("Masukkan persentase kehadiran: "))

if nilai >= 60 and kehadiran >= 80:
    print("Lulus")
else:
    print("Belum lulus")