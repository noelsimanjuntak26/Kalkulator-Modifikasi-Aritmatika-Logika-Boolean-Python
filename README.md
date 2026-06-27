
# 🧮 LogiCalc: CLI Arithmetic & Boolean Calculator

Kalkulator berbasis Command-Line Interface (CLI) yang dibangun menggunakan Python. Project ini memodifikasi fungsi kalkulator standar dengan menggabungkan operasi matematika dasar (aritmatika) dan operasi logika boolean dalam satu program yang interaktif, cerdas, dan tangguh.

---

## ✨ Fitur Utama

- **Robust Input Validation:** Menggunakan mekanisme validasi string (`.lower().strip()`) sehingga program tidak sensitif terhadap spasi liar maupun variasi huruf kapital yang tidak sengaja diketik oleh pengguna.
- **7 Operasi Aritmatika Lengkap:** Mendukung Penjumlahan (`+`), Pengurangan (`-`), Perkalian (`*`), Pembagian (`/`), Perpangkatan (`**`), Sisa Bagi/Modulus (`%`), dan Pembagian Bulat/Floor Division (`//`).
- **Dynamic Boolean Logic Evaluation:** Mendukung operasi logika dua subjek (`AND`, `OR`, `XOR`) serta operator satu subjek (`NOT`).
- **Smart Control Flow:** Program secara otomatis mendeteksi jenis operator logika. Jika memilih operator `NOT`, kalkulator hanya akan meminta 1 input variabel tanpa memaksa user memasukkan input kedua.
- **Type Casting Safety:** Mengonversi input teks string (`"True"`/`"False"`) secara dinamis menjadi tipe data Boolean asli Python sebelum dievaluasi.

---

## 🛠️ Teknologi yang Digunakan

- **Bahasa Pemrograman:** Python 3.x
- **Paradigma:** Procedural Programming / Imperative Logic
- **Built-in Functions & Methods:** `input()`, `int()`, `print()`, `.lower()`, `.strip()`, Logical operators (`and`, `or`, `not`, `^`).

---

## 📋 Prasyarat & Instalasi

Sebelum menjalankan project ini, pastikan kamu sudah menginstal Python di perangkat komputermu.

### Prasyarat
- Python versi 3.6 ke atas.

### Langkah Instalasi
1. Buka terminal atau Command Prompt (CMD).
2. Clone repository ini ke komputer lokalmu:
   ```bash
   git clone https://github.com/noelsimanjuntak26/Kalkulator-Modifikasi-Aritmatika-Logika-Boolean-Python.git
3. Masuk ke direktori project:
   ```bash
   cd Kalkulator-Modifikasi-Aritmatika-Logika-Boolean-Python


---

## 📁 Susunan Project

Struktur berkas di dalam repository ini sangat sederhana dan minimalis:

```text
Kalkulator-Modifikasi-Aritmatika-Logika-Boolean-Python/
│
├── main.py          # File utama kode program kalkulator
└── README.md        # Dokumentasi panduan project (file ini)

```

---

## 🚀 Penggunaan

Untuk menjalankan kalkulator, ketik perintah berikut pada terminal di dalam direktori project:

```bash
python main.py

```

### Contoh Alur Operasi Aritmatika:

1. Jalankan program, ketik `operasi aritmatika`.
2. Pilih operator, misalnya `** (pangkat)`.
3. Masukkan angka pertama: `2`.
4. Masukkan angka kedua: `3`.
5. Program akan mengeluarkan hasil: `hasil dari 2 ** 3 = 8`.

### Contoh Alur Operasi Logika Boolean:

1. Jalankan program, ketik `operasi logika boolean`.
2. Pilih operator, misalnya `not`.
3. Masukkan pilihan pertama: `True`.
4. Program langsung memproses tanpa meminta input kedua: `hasil dari not True = False`.

---

## 🤝 Kontribusi

Kontribusi selalu terbuka untuk siapa saja! Jika kamu menemukan bug, memiliki ide fitur baru, atau ingin mengoptimalkan kode ini, silakan ikuti langkah-langkah berikut:

1. Lakukan **Fork** pada repository ini.
2. Buat branch fitur baru kamu (`git checkout -b fitur-keren-kamu`).
3. Commit perubahan yang kamu buat (`git commit -m 'Menambahkan fitur X'`).
4. Push ke branch tersebut (`git push origin fitur-keren-kamu`).
5. Buka sebuah **Pull Request** di GitHub.

---

## 📄 Lisensi

Project ini dilisensikan di bawah **Lisensi MIT**. Anda bebas untuk menggunakan, mengubah, dan mendistribusikan kode ini untuk keperluan pribadi maupun komersial.

```text
MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
