# 02_bandingkan_dua_bilangan.py

a = float(input("Masukkan bilangan pertama: "))
b = float(input("Masukkan bilangan kedua: "))

if a >= b:
    if a == b:
        print("Kedua bilangan sama.")
    else:
        print("Bilangan pertama lebih besar dari bilangan kedua.")
else:
    print("Bilangan pertama lebih kecil dari bilangan kedua.")