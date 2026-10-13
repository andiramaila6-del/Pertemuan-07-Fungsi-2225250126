def luas_persegi_panjang(p, l):
    return p * l


def luas_segitiga(a, t):
    return 0.5 * a * t


def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def faktorial(n):
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil


def tampilkan_menu():
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")
    print("0. Keluar")


# Program utama
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        p = float(input("Masukkan panjang: "))
        l = float(input("Masukkan lebar: "))
        print("Luas =", luas_persegi_panjang(p, l))

    elif pilihan == "2":
        a = float(input("Masukkan alas: "))
        t = float(input("Masukkan tinggi: "))
        print("Luas =", luas_segitiga(a, t))

    elif pilihan == "3":
        try:
            n = int(input("Masukkan n: "))
            if n < 0:
                print("n harus bilangan bulat nonnegatif.")
            else:
                print("Jumlah =", jumlah_n(n))
        except ValueError:
            print("Input harus berupa bilangan bulat.")

    elif pilihan == "4":
        try:
            n = int(input("Masukkan n: "))
            if n < 0:
                print("n harus bilangan bulat nonnegatif.")
            else:
                print("Faktorial =", faktorial(n))
        except ValueError:
            print("Input harus berupa bilangan bulat.")

    elif pilihan == "0":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")

    print()