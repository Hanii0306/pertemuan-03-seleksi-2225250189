# analisis_persamaan_kuadrat.py

import math

print("=" * 50)
print("ANALISIS PERSAMAAN KUADRAT")
print("Bentuk umum: ax^2 + bx + c = 0")
print("=" * 50)

# Input koefisien
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))

print("\n" + "=" * 50)
print("HASIL ANALISIS")
print("=" * 50)

# Memeriksa apakah persamaan merupakan persamaan kuadrat
if a == 0:
    print("Nilai a tidak boleh 0.")
    print("Karena a = 0, persamaan bukan merupakan persamaan kuadrat.")

else:
    # Menghitung diskriminan
    D = b**2 - 4*a*c

    print(f"Persamaan: {a}x^2 + ({b})x + ({c}) = 0")
    print(f"Diskriminan (D) = {D}")

    # Menentukan jenis akar berdasarkan diskriminan
    if D > 0:

        # Dua akar real berbeda
        akar1 = (-b + math.sqrt(D)) / (2 * a)
        akar2 = (-b - math.sqrt(D)) / (2 * a)

        print("Jenis akar: Dua akar real berbeda")
        print(f"x1 = {akar1}")
        print(f"x2 = {akar2}")

        # Menentukan apakah akar positif/negatif
        if akar1 > 0 and akar2 > 0:
            print("Kedua akar bernilai positif.")

        elif akar1 < 0 and akar2 < 0:
            print("Kedua akar bernilai negatif.")

        else:
            print("Satu akar positif dan satu akar negatif.")

    elif D == 0:

        # Satu akar real kembar
        akar = -b / (2 * a)

        print("Jenis akar: Akar real kembar")
        print(f"x1 = x2 = {akar}")

        if akar > 0:
            print("Akar bernilai positif.")

        elif akar < 0:
            print("Akar bernilai negatif.")

        else:
            print("Akar bernilai nol.")

    else:

        # Tidak mempunyai akar real
        print("Jenis akar: Tidak mempunyai akar real")
        print("Persamaan memiliki dua akar kompleks.")

        # Menghitung bagian real dan imajiner
        bagian_real = -b / (2 * a)
        bagian_imajiner = math.sqrt(-D) / abs(2 * a)

        print(f"Bagian real = {bagian_real}")
        print(f"Bagian imajiner = {bagian_imajiner}")

        print(
            f"x1 = {bagian_real} + {bagian_imajiner}i"
        )
        print(
            f"x2 = {bagian_real} - {bagian_imajiner}i"
        )

    # Menentukan sumbu simetri
    sumbu_simetri = -b / (2 * a)

    # Menentukan titik puncak
    nilai_y = a * sumbu_simetri**2 + b * sumbu_simetri + c

    print("\n" + "=" * 50)
    print("INFORMASI TAMBAHAN")
    print("=" * 50)

    print(f"Sumbu simetri = x = {sumbu_simetri}")
    print(
        f"Titik puncak = ({sumbu_simetri}, {nilai_y})"
    )

    # Menentukan arah parabola
    if a > 0:
        print("Parabola terbuka ke atas.")
        print("Titik puncak merupakan titik minimum.")
    else:
        print("Parabola terbuka ke bawah.")
        print("Titik puncak merupakan titik maksimum.")

print("\nProgram selesai.")