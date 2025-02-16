# Hotel Management System

Sistem manajemen hotel ini memungkinkan pengelola dan pengunjung untuk berinteraksi dengan daftar hotel yang telah tersedia. Sistem ini memiliki beberapa fitur utama, seperti menampilkan daftar hotel, menambah dan mengelola data hotel, serta memesan kamar dengan opsi diskon menggunakan voucher.

## **Flowchart Sistem**
![Flowchart](https://github.com/user-attachments/assets/0f054adb-ad5f-4f5b-825f-2767c5f6520e)

---

## **Komponen Utama**

### **1. Data yang Digunakan**
- **`daftar_hotel`**: Berisi daftar hotel dalam bentuk dictionary di dalam list yang mencakup ID, nama, bintang, lokasi, harga, dan jumlah kamar yang tersedia.
- **`voucher_list`**: Berisi daftar voucher diskon dalam bentuk dictionary di dalam list yang mencakup kode voucher dan persentase diskon.

### **2. Pengguna**
- **Admin**: 
  - Menambah, mengedit, dan menghapus data hotel.
  - Melihat daftar hotel.
  - Melihat pemesanan kamar hotel.
- **Pengunjung**:
  - Melihat daftar hotel.
  - Melakukan pemesanan kamar.

---

## **Fitur Program**

### **1. Tampilkan Daftar Hotel**
Menu ini menampilkan daftar hotel berdasarkan berbagai kriteria:
- **Menu 1:** Menampilkan semua daftar hotel (ID, nama, bintang, lokasi, harga, jumlah kamar).
- **Menu 2:** Menampilkan daftar berdasarkan rentang harga.
- **Menu 3:** Menampilkan daftar berdasarkan lokasi.
- **Menu 4:** Menampilkan daftar berdasarkan bintang (1-5).
- **Menu 5:** Menampilkan daftar berdasarkan urutan harga (tertinggi/terendah).

![Daftar Hotel](https://github.com/user-attachments/assets/9345ba54-7235-4dd4-83a9-4f682a278c21)

---

### **2. Tambah Hotel**
Fitur ini memungkinkan admin untuk menambahkan hotel baru dengan memasukkan ID hotel, nama, bintang, lokasi, harga, dan jumlah kamar yang tersedia.

![Tambah Hotel](https://github.com/user-attachments/assets/dcc1da04-7dad-4c66-a4c9-bfbbc3d3c9e2)

---

### **3. Hapus Hotel**
Admin dapat menghapus data hotel berdasarkan ID yang dimasukkan.

![Hapus Hotel](https://github.com/user-attachments/assets/7f39adc5-476f-4c61-b745-f7d73e472c24)

---

### **4. Edit Hotel**
Admin dapat memperbarui informasi hotel berdasarkan ID yang dipilih, termasuk nama, bintang, lokasi, harga, dan jumlah kamar.

![Edit Hotel](https://github.com/user-attachments/assets/80cb8a87-7fe9-4e0d-8193-1dc03eb4a6a7)

---

### **5. Pemesanan Kamar**
Pengguna dapat melakukan pemesanan kamar, melihat status pemesanan, dan melakukan pembayaran dengan voucher diskon jika tersedia.

- **Menu Pemesanan:** Pengguna memilih kamar yang ingin dipesan dan dapat menggunakan kode voucher untuk diskon.
- **Cek Status Pemesanan:** Pengguna dapat melihat daftar kamar yang telah dipesan.

![Pemesanan Kamar](https://github.com/user-attachments/assets/0a3b7cb4-d764-4b03-a3c9-bc7bf05c83b1)
