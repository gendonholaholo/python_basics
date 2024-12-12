# Jangan pusing, inti dari konsep "File Handling" hanya bagaimana cara kita memberi hak akses membaca, menulis, menambah, membuka gambar (biner), membuka file dan menulis jika belum ada
# Kywords yang wajib diingat:
# r = membuka file untuk dibaca
# w = membuka file untuk menulis (akan membuat file baru & menimpa file yang ada)
# a = membuka fule untuk menambhkan ke file yang ada
# b = mode biner, membuka gambar misalnya
# x = membuka file untuk menulis & membuat file baru jika belum ada dan bila sudah ada malah error

# Penggunaan dasar
# Membaca seluruh isi file
with open("./dataLatihan/data.txt", "r") as file:
    content = file.read()
    print(content)

# Membaca per baris
with open("./dataLatihan/data.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip()) # Menghilangkan karakter newline
# ____________________________________________________________________________________________________________________________________


# Menulis ke file (mengganti isi file)
with open("./dataLatihan/menyapa.txt", "w") as file:
    file.write("Hello, Lisa!\n")
    file.write("Ini adalah file baru.\n")

# Menulis beberapa baris sekaligus
lines = ["Baris 1\n",
         "Baris 2\n",
         "Baris 3\n"]
with open("./dataLatihan/outputBaris.txt", "w") as file:
    file.writelines(lines)
# ____________________________________________________________________________________________________________________________________


# Menambah konten ke dalam file
with open("./dataLatihan/menyapa.txt", "a") as file:
    file.write("\nIni baris baru\n")
# ____________________________________________________________________________________________________________________________________


# Menutup file
file = open("./dataLatihan/menyapa.txt", "r")
content = file.read()
print(content)
file.close()
