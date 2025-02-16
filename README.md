# Hotel-Management-System

Program ini adalah sistem manajemen hotel yang memungkinkan pengelola dan pengunjung untuk berinteraksi dengan daftar hotel yang telah disediakan. Sistem ini memiliki beberapa fitur utama, termasuk menampilkan daftar hotel, menambahkan dan mengelola data hotel, serta memesan kamar dengan opsi diskon menggunakan voucher. Berikut merupakan flowchart dari sistem yang telah dibuat:
![image](https://github.com/user-attachments/assets/0f054adb-ad5f-4f5b-825f-2767c5f6520e)

### **Komponen Utama:**
1. **Data yang digunakan**
   - `daftar hotel`: Berisi daftar hotel dalam bentuk dictionary di dalam list yang mencakup ID, nama, bintang, lokasi, harga, dan jumlah kamar yang tersedia.
   - `voucher_list`: Berisi daftar voucher diskon dalam bentuk dictionary di dalam list yang dapat digunakan saat pemesanan mencakup kode voucher dan persentase diskon.

2. **Pengguna**
   - **Admin**: Memiliki akses untuk menambah, mengedit, dan menghapus data hotel, serta melihat daftar hotel dan melihat pemesanan kamar hotel.
   - **Pengunjung**: Memiliki akses untuk melihat daftar hotel, melakukan pemesanan kamar.

### **Fitur Program**
1. **Tampilkan Daftar Hotel**: 
   < br / > Menu untuk menampilkan daftar hotel berdasarkan kriteria yang dipilih.
   - **Menu 1:** Menampilkan Semua Daftar Hotel yang mencakup ID, nama, bintang, lokasi, harga, dan jumlah kamar yang tersedia
   - **Menu 2:** Menampilkan Daftar Berdasarkan Range Harga dengan memasukkan harga minimum dan maksimum.
   - **Menu 3:** Menampilkan Daftar Berdasarkan Lokasi dengan memasukkan lokasi hotel yang ingin dilihat.
   - **Menu 4:** Menampilkan Daftar Berdasarkan Bintang dengan memasukkan bintang hotel (1-5).
   - **Menu 5:** Menampilkan Berdasarkan Urutan harga tertinggi atau terendah.

![image](https://github.com/user-attachments/assets/9345ba54-7235-4dd4-83a9-4f682a278c21)

2. **Tambah Hotel**
   < br / > Menu ini memungkinkan pengelola (admin) untuk menambahkan daftar hotel baru ke dalam sistem. Data yang dimasukkan berupa ID hotel yang bersifat unik value, nama, bintang, lokasi, harga, dan jumlah kamar yang tersedia di hotel tersebut
![image](https://github.com/user-attachments/assets/dcc1da04-7dad-4c66-a4c9-bfbbc3d3c9e2)

4. **Hapus Hotel**
   < br / > Menu ini memungkinkan pengelola (admin) untuk menghapus data hotel dari daftar yang tersimpan dalam daftar_hotel berdasarkan ID yang dimasukkan.

![image](https://github.com/user-attachments/assets/7f39adc5-476f-4c61-b745-f7d73e472c24)

6. **Edit Hotel**
   < br / > Menu ini memungkinkan pengelola (admin) untuk mengedit data hotel yang tersimpan dalam daftar daftar_hotel. Fungsi ini memungkinkan pengguna untuk memperbarui informasi tertentu berdasarkan ID hotel. Menu edit ini dibagi berdasarkan fitur data yang bisa diganti seperti nama, bintang, lokasi, harga, dan jumlah kamar hotel yang ada di dalam list daftar_hotel.
![image](https://github.com/user-attachments/assets/80cb8a87-7fe9-4e0d-8193-1dc03eb4a6a7)

8. **Pemesanan Kamar**
   < br / > Menu ini memungkinkan pengguna dan pengelola untuk memesan kamar hotel, melihat status pemesanan, dan melakukan pembayaran.
   - **Menu Pemesanan:** Sistem akan menampilkan daftar hotel yang tersedia, lalu pengguna akan memilih satu atau beberapa kamar hotel yang akan dipesan. Setelah melakukan pemesanan pengguna dapat melakukan pembayaran dan dapat menggunakan kode voucher untuk mendapatkan potongan harga.
   - **Cek Status Pemesanan:** Setelah melakukan pemesanan pengguna dapat melihat daftar kamar hotel yang telah dipesannya

![image](https://github.com/user-attachments/assets/0a3b7cb4-d764-4b03-a3c9-bc7bf05c83b1)

