# 04_jenis_segitiga.py

a = float(input("Masukkan panjang sisi a: "))
b = float(input("Masukkan panjang sisi b: "))
c = float(input("Masukkan panjang sisi c: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Panjang sisi harus lebih besar dari 0.")
else:
    if a + b > c and a + c > b and b + c > a:

        if a == b and b == c:
            print("Segitiga sama sisi.")

        else:
            if a == b or a == c or b == c:
                print("Segitiga sama kaki.")
            else:
                print("Segitiga sembarang.")

    else:
        print("Ketiga sisi tersebut tidak dapat membentuk segitiga.")