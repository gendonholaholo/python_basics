print("\033[4mExceptoin Handling\033[0m\n")

print("\033[4mPenggunaan 1 | Penggunaan biasa\033[0m")
try:
    # Block code yang berpotensi menimbulkan error
    angka = int(input("Masukan angka: "))
    print("Angka yang dimasukkan", angka)
except ValueError:
    # Jika terjadi error (ValueError), program akan menampilkan pesan berikut
    print("Terjadi kesalahan! Harap masukkan angka yang valid.")

print("\n\033[4mPenggunaan 2 | Multi except\033[0m")
try:
    x = int(input("Masukkan angka pertama: "))
    y = int(input("Masukkan angka kedua: "))
    hasil = x/y
    print("Hasil pembagian:", hasil)
except ValueError:
    # Error yang menangkap jika input bukan angka
    print("Kesalahan: Harap masukkan angka yang valid.")
except ZeroDivisionError:
    # Error yang menangkap jika pembagian dilakukan dengan 0
    print("Kesalahan: Tidak dapat membagi dengan nol.")
except ZeroDivisionError:
    # Menangkap error yang bukan dari 2 di atas
    Print(f"Terjadi kesalahan yang tidak diketahui: {e}")

print("\n\033[4mPenggunaan 3 | Menggunakan else\033[0m")
try:
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
    hasil = angka1 + angka2
except ValueError:
    print("Keslahan: Harap masukkan angka yang valid.")
else:
    # Jika tidak ada exception, blok ini dijalankan
    print("Hasil penjumlahan:", hasil)


print("\n\033[4mPenggunaan 4 | Menggunakan finally\033[0m")
try:
    angka = int(input("Masukkan angka: "))
    hasil = 10/angka
    print(f"Hasil pembagian 10 dengan {angka} adalah {hasil}")
except ValueError as e:
    print(f"terjadi Kesalahan: {e}. Input yang dimasukan bukan angka.")
except ZeroDivisionError as e:
    print(f"Terjadi kesalahan: {e}. Tidak bisa membagi dengan angka 0")
except Exception as e:
    print(f"Terjadi kesalahan yang tidak terduga: {e}")
else:
    print("Pembagian berhasil dilakukan.")
finally:
    print("Terima kasih telah mencoba program ini!")

