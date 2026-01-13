# 📊 Aplikasi Web Sistem Antrian M/M/2
Aplikasi ini merupakan aplikasi web berbasis Python yang digunakan untuk menghitung parameter sistem antrian

**M/M/2 (dua pelayan)**
berdasarkan teori antrian. Aplikasi ini dibuat untuk membantu memahami kinerja sistem pelayanan dengan dua server menggunakan perhitungan matematis sesuai teori.
Aplikasi menerima input berupa waktu antar kedatangan pelanggan dan waktu pelayanan per pelayan, kemudian menampilkan hasil perhitungan secara otomatis dan sistematis.

---

## 👤 Identitas Pembuat
* **Nama:** Ardi Kamal Karima
* **NIM:** 31230023
* **Kelas:** 5C
* **Program Studi:** S1 Teknik Informatika
* **Fakultas:** Teknologi Informasi
* **Universitas:** Universitas Bale Bandung (UNIBBA)

---

## ⚙️ Teknologi yang Digunakan
* Python 3
* Flask
* HTML
* CSS

---

## 📁 Struktur Folder Proyek
```
MM2_QUEUE_APP/
│
├── app.py
├── requirements.txt
│
├── templates/
│   ├── input.html
│   └── result.html
│
└── static/
    └── style.css
```

---

## 🧮 Model Antrian M/M/2
Karakteristik model:
* Kedatangan pelanggan mengikuti distribusi **Poisson**
* Waktu pelayanan mengikuti distribusi **Eksponensial**
* Jumlah pelayan: **2 server**
* Disiplin antrian: **First Come First Served (FCFS)**

Rumus yang digunakan:
* Laju kedatangan (λ):
  λ = 1 / waktu antar kedatangan
* Laju pelayanan (μ):
  μ = 1 / waktu pelayanan
* Utilisasi sistem (ρ):
  ρ = λ / (2μ)
* Waktu rata-rata dalam sistem (W):
  W = 1 / (μ − λ/2)
* Waktu rata-rata dalam antrian (Wq):
  Wq = λ² / [2μ(μ − λ/2)]
Sistem dikatakan stabil jika **ρ < 1**.

---

## ▶️ Cara Menjalankan Aplikasi
### 1. Install Library
```bash
pip install -r requirements.txt
```
### 2. Jalankan Program
```bash
python app.py
```
### 3. Buka di Browser
```
http://127.0.0.1:5000
```
---

## 📝 Cara Menggunakan Aplikasi
1. Masukkan waktu antar kedatangan (menit)
2. Masukkan waktu pelayanan per pelayan (menit)
3. Klik tombol **Hitung Antrian**
4. Sistem akan menampilkan:
   * Laju kedatangan (λ)
   * Laju pelayanan (μ)
   * Utilisasi sistem (ρ)
   * Waktu rata-rata dalam sistem (W)
   * Waktu rata-rata dalam antrian (Wq)
   * Langkah perhitungan
Jika sistem tidak stabil, aplikasi akan menampilkan peringatan.

---

## 📊 Perbandingan dengan Perhitungan Manual
Hasil perhitungan aplikasi sesuai dengan perhitungan manual karena menggunakan rumus teori antrian M/M/2 secara langsung.
Tidak terdapat perbedaan hasil karena tidak menggunakan simulasi acak, melainkan perhitungan matematis deterministik.

---

## 🎯 Tujuan Aplikasi
Aplikasi ini bertujuan untuk membantu mahasiswa dalam memahami:
* Konsep sistem antrian dua pelayan
* Pengaruh tingkat kedatangan terhadap waktu tunggu
* Evaluasi kinerja sistem pelayanan

---

## 📜 Lisensi
Proyek ini dibuat untuk keperluan pendidikan dan pembelajaran.

---
