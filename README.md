Pertemuan 07 Fungsi Python

Nama: Maila Andira Putri
NIM: 2225250126
Kelas: 3A

1. Tujuan

Praktikum ini bertujuan untuk memahami penggunaan fungsi, parameter, argumen, return value, dan scope variabel dalam Python. Melalui praktikum ini, program dibagi menjadi beberapa fungsi agar setiap bagian memiliki tugas yang jelas. Selain itu, praktikum ini melatih penggunaan perulangan, seleksi kondisi, pengujian program, serta dokumentasi menggunakan Git dan GitHub.

2. Cara Menjalankan

Program dibuat menggunakan Visual Studio Code dengan bahasa pemrograman Python 3.

Langkah-langkah menjalankan program:

1. Membuka folder proyek Pertemuan 07 di VS Code.
2. Memastikan Python sudah terpasang.
3. Membuka file Python yang akan dijalankan.
4. Membuka terminal melalui menu Terminal > New Terminal.
5. Menjalankan program menggunakan perintah berikut.

python Praktik/utilitas_matematika.py

6. Memilih operasi matematika melalui menu yang ditampilkan.
7. Memasukkan nilai sesuai permintaan program dan memeriksa hasilnya.

3. Struktur Folder

Struktur folder proyek yang digunakan adalah sebagai berikut.

Pertemuan-07-Fungsi-2225250126/
├── .gitignore
├── README.md
├── latihan/
│   ├── 01_salam.py
│   ├── 02_luas_persegi_panjang.py
│   ├── 03_jumlah_n.py
│   ├── 04_statistik_sederhana.py
│   └── 05_scope.py
└── praktik/
    └── utilitas_matematika.py

Folder latihan berisi lima program untuk mempelajari fungsi salam, luas persegi panjang, jumlah bilangan, statistik sederhana, dan scope variabel. Folder praktik berisi program utilitas matematika modular yang menggabungkan beberapa fungsi dalam satu program berbasis menu.

4. Struktur Fungsi

4.1 Fungsi luas_persegi_panjang(p, l)

Fungsi ini digunakan untuk menghitung luas persegi panjang dengan mengalikan panjang dan lebar.

- Parameter: "p" sebagai panjang dan "l" sebagai lebar.
- Proses: menghitung "p * l".
- Return value: hasil perkalian panjang dan lebar.

4.2 Fungsi luas_segitiga(a, t)

Fungsi ini digunakan untuk menghitung luas segitiga.

- Parameter: "a" sebagai alas dan "t" sebagai tinggi.
- Proses: menghitung "0.5 * a * t".
- Return value: hasil perhitungan luas segitiga.

4.3 Fungsi jumlah_n(n)

Fungsi ini digunakan untuk menghitung jumlah bilangan dari 1 sampai n.

- Parameter: "n" sebagai batas bilangan.
- Proses: menggunakan perulangan "for" untuk menjumlahkan bilangan dari 1 sampai n.
- Return value: jumlah seluruh bilangan yang dihitung.

4.4 Fungsi faktorial(n)

Fungsi ini digunakan untuk menghitung faktorial suatu bilangan bulat nonnegatif.

- Parameter: "n" sebagai bilangan yang akan dihitung faktorialnya.
- Proses: menggunakan perulangan untuk mengalikan bilangan dari 2 sampai n.
- Return value: hasil faktorial. Untuk n = 0, hasilnya adalah 1.

4.5 Fungsi tampilkan_menu()

Fungsi ini digunakan untuk menampilkan daftar pilihan operasi matematika kepada pengguna. Fungsi ini tidak memerlukan parameter dan bertugas menampilkan menu sebelum pengguna memilih operasi.

4.6 Program Utama

Program utama menggunakan perintah "input()" untuk menerima pilihan pengguna. Seleksi "if", "elif", dan "else" digunakan untuk menentukan fungsi yang dijalankan sesuai pilihan. Program juga menyediakan pilihan keluar agar pengguna dapat mengakhiri program.

5. Hasil Pengujian

Pengujian dilakukan dengan membandingkan hasil yang diharapkan dengan hasil aktual dari program.

No.| Operasi| Input| Hasil yang Diharapkan| Hasil Aktual| Status
1| Luas persegi panjang| p=8, l=5| 40| 40| Berhasil
2| Luas segitiga| a=10, t=6| 30.0| 30.0| Berhasil
3| Jumlah 1 sampai n| n=10| 55| 55| Berhasil
4| Faktorial| n=5| 120| 120| Berhasil
5| Faktorial| n=0| 1| 1| Berhasil

Berdasarkan test case tersebut, program diharapkan menghasilkan keluaran sesuai perhitungan matematika. Pengujian dilakukan untuk memastikan bahwa setiap fungsi memberikan hasil yang benar, termasuk kasus khusus faktorial dengan input nol.

6. Konsep yang Dipelajari

6.1 Fungsi

Fungsi merupakan bagian program yang dibuat untuk menjalankan tugas tertentu. Penggunaan fungsi membantu mengurangi pengulangan kode dan membuat program lebih mudah dibaca.

6.2 Parameter dan Argumen

Parameter merupakan variabel yang dituliskan pada definisi fungsi, sedangkan argumen merupakan nilai yang diberikan ketika fungsi dipanggil. Keduanya memungkinkan fungsi digunakan dengan data yang berbeda.

6.3 Return Value

Perintah "return" digunakan untuk mengembalikan hasil dari suatu fungsi. Hasil tersebut dapat disimpan dalam variabel atau digunakan dalam proses lain.

6.4 Scope Variabel

Scope menentukan bagian program yang dapat mengakses suatu variabel. Variabel lokal dibuat di dalam fungsi dan digunakan untuk kebutuhan proses fungsi tersebut.

6.5 Perulangan dan Seleksi

Perulangan "for" digunakan dalam fungsi jumlah_n dan faktorial. Sementara itu, seleksi kondisi digunakan untuk menjalankan operasi berdasarkan pilihan pengguna.

7. Refleksi

Setelah mempelajari fungsi dalam Python, saya memahami bahwa program dapat dibuat lebih terstruktur dengan membagi setiap proses ke dalam fungsi yang berbeda. Setiap fungsi memiliki tugas dan parameter masing-masing sehingga rumus tidak perlu ditulis berulang kali. Penggunaan "return" juga memungkinkan hasil perhitungan digunakan kembali oleh bagian program lain.

Melalui praktikum ini, saya juga mempelajari cara menggunakan perulangan untuk melakukan perhitungan berulang dan seleksi kondisi untuk membuat program berbasis menu. Pengujian dengan beberapa input membantu memastikan bahwa hasil perhitungan sudah sesuai dengan yang diharapkan. Dengan demikian, program menjadi lebih mudah dipahami, diuji, dan diperbaiki.

8. Kesimpulan

Praktikum Pertemuan 07 memberikan pemahaman mengenai penggunaan fungsi, parameter, return value, dan scope variabel dalam Python. Program utilitas matematika menunjukkan bahwa beberapa operasi dapat dipisahkan menjadi fungsi-fungsi sederhana dan dipanggil melalui menu. Dengan struktur yang modular, kode menjadi lebih rapi, mudah digunakan kembali, dan lebih mudah diuji.