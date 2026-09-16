# Pertemuan 03 - Seleksi

## Identitas

**Nama:** Umul Hani
**NIM:** 2225250189
**Kelas:** 3F

---

## Tujuan Pembelajaran

Setelah menyelesaikan kegiatan ini, mahasiswa diharapkan mampu:

1. Memahami konsep struktur seleksi dalam algoritma pemrograman.
2. Menggunakan struktur `if`, `if-else`, dan `if-elif-else` dalam Python.
3. Menggunakan operator perbandingan dan operator logika.
4. Menerapkan nested `if` untuk menyelesaikan permasalahan.
5. Membuat program sederhana berdasarkan kondisi yang diberikan.
6. Menguji program menggunakan beberapa contoh kasus.

---

## Cara Menjalankan

1. Buka folder project **`pertemuan-03-seleksi-NIM`** di VS Code.
2. Pastikan Python sudah terpasang pada komputer.
3. Buka terminal di VS Code.
4. Jalankan file latihan dengan perintah:

```bash
python latihan/01_genap_ganjil.py
```

Untuk latihan lainnya:

```bash
python latihan/02_bandingkan_dua_bilangan.py
python latihan/03_kelulusan_bersyarat.py
python latihan/04_jenis_segitiga.py
```

Untuk menjalankan tugas:

```bash
python tugas/analisis_persamaan_kuadrat.py
```

---

## Algoritma Tugas

### Analisis Persamaan Kuadrat

Program digunakan untuk menganalisis persamaan kuadrat dengan bentuk umum:

```text
ax² + bx + c = 0
```

### Langkah Algoritma

1. Mulai.
2. Masukkan nilai koefisien `a`, `b`, dan `c`.
3. Periksa nilai `a`.
4. Jika `a = 0`, maka persamaan bukan merupakan persamaan kuadrat.
5. Jika `a ≠ 0`, hitung diskriminan dengan rumus:

```text
D = b² - 4ac
```

6. Periksa nilai diskriminan:

   * Jika `D > 0`, maka terdapat dua akar real berbeda.
   * Jika `D = 0`, maka terdapat satu akar real kembar.
   * Jika `D < 0`, maka tidak terdapat akar real.
7. Hitung akar sesuai dengan kondisi diskriminan.
8. Tentukan sumbu simetri:

```text
x = -b / 2a
```

9. Tentukan titik puncak parabola.
10. Tentukan arah parabola berdasarkan nilai `a`.
11. Tampilkan hasil analisis.
12. Selesai.

---

## Hasil Pengujian

### Pengujian 1

Input:

```text
a = 1
b = -5
c = 6
```

Hasil:

```text
Diskriminan = 1
Jenis akar = Dua akar real berbeda
x1 = 3
x2 = 2
```

### Pengujian 2

Input:

```text
a = 1
b = -4
c = 4
```

Hasil:

```text
Diskriminan = 0
Jenis akar = Akar real kembar
x1 = x2 = 2
```

### Pengujian 3

Input:

```text
a = 1
b = 2
c = 5
```

Hasil:

```text
Diskriminan = -16
Jenis akar = Tidak mempunyai akar real
```

### Pengujian 4

Input:

```text
a = 0
b = 2
c = 3
```

Hasil:

```text
Nilai a tidak boleh 0.
Persamaan bukan merupakan persamaan kuadrat.
```

---

## Refleksi

Setelah mengerjakan tugas ini, saya memahami bahwa struktur seleksi digunakan untuk membuat program dapat mengambil keputusan berdasarkan kondisi tertentu. Pada tugas analisis persamaan kuadrat, struktur `if`, `elif`, dan `else` digunakan untuk menentukan jenis akar berdasarkan nilai diskriminan.

Saya juga memahami penggunaan operator perbandingan serta penerapan rumus matematika ke dalam bahasa pemrograman Python. Melalui beberapa pengujian, saya dapat mengetahui bahwa program harus menangani kondisi yang berbeda, seperti dua akar real berbeda, akar real kembar, tidak memiliki akar real, dan kondisi ketika nilai `a` sama dengan nol.

Kegiatan ini membantu saya memahami hubungan antara algoritma, logika percabangan, dan implementasi program Python.
