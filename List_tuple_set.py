print("\033[4mList\033[0m\n")

# List adalah urutan terurut yang dapat diubah (mutable), dan bisa berisi berbagai tipe data.
# Elemen-elemen dalam list dipisahkan dengan koma dan dibungkus dengan tanda kurung siku [].

my_lisa = [10,20,30,40,50]

print("Contoh List:", my_lisa)

# Menambahkan elemen baru ke dalam list
my_lisa.append(60)
print("List setelah append:", my_lisa)

# Mengakses elemen menggunakan indeks
print("Elemen pertama dalam list:", my_lisa[0])

# Mengubah nilai elemen dalam list
my_lisa[1] = 25
print("List setelah perubahan elemen:", my_lisa)

#________________________________________________#

print("\n\033[4mTuple\033[0m\n")

# Tuple adalah urutan terurut yang tidak dapat diubah (immutable), dan bisa berisi berbagai tipe data.
# Elemen-elemen dalam tuple dipisahkan dengan koma dan dibungkus dengan tanda kurung biasa ().

my_leo = (1,2,3,4,5)

print("Contoh Tuple:", my_leo[2])

# Karena tuple tidak bisa diubah (immutable), maka kita tidak bisa melakukan operasi append ataupun mengubah nilai elemen
# Contoh: my_leo[1] = 10 -> maka ini akan mengembalikan error

#________________________________________________#

print("\n\033[4mSet\033[0m\n")

# Set adalah koleksi tidak terurut yang tidak dapat memiliki elemen duplikat.
# Set dibungkus dengan tanda kurung kurawal {}.

my_gos = {10,20,30,40,50}

print("Contoh Set:", my_gos)

# Menambahkan elemen baru dalam set
my_gos.add(60)
print("Set setelah add:", my_gos)

# Set tidak mendukung akses elemen menggunakan indeks karena tidak terurut
# Tetapi kita bisa mengecek apakah suatu lemen ada dalam set
print("Apakah 30 ada dalam set?", 30 in my_gos)

# Menghapus elemen dari set
my_gos.remove(20)
print("Set setelah menghapus 20:", my_gos)
