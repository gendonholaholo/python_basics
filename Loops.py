# Iterasi dari list (for loop)
print("\033[4mFor Loop\033[0m\n")

print("\033[4mContoh 1\033[0m\n")
buah = ["apel", "jeruk", "pisang", "mangga"]
for buah in buah:
    print(buah) # Menampilkan setial elemen dalam list 'buah'

print("\n\033[4mContoh 2\033[0m\n")

for x in range(1, 5):
    print(x) # Menampilkan angka dari satu sampai 4

#___________________________________________________________________________#

# Penggunaan dalam kondisi tertentu (while loop)
print("\n\033[4mWhile Loop\033[0m\n")

print("\033[4mContoh 1\033[0m")
menghitung = 1
while menghitung <= 5:
    print(menghitung) # Menampilkan dari 1-5
    menghitung += 1

print("\n\033[4mContoh 2\033[0m")

angka = 0
while angka != -1:
    angka = int(input("Masukan angka (-1 untuk berhenti): "))
    print(f"Angka yang dimasukkan: {angka}")

#___________________________________________________________________________#

# Mencetak tabel perkalian (nested loop)
print("\n\033[4mNested Loop\033[0m\n")

for i in range(1, 4): # Perulangan baris (1-3)
    for j in range (1, 4): # Perulangan kolom (1-3)
       print(f"{i} x {j} = {i*j}", end="\t")
    print() # Berpindah baris saat satu baris selesai diproses
    
#___________________________________________________________________________#

# Penggunaan break untuk keluar dari loop
print("\n\033[4mBreak Statement\033[0m\n")

for gos in range(1, 10):
    if gos == 5:
        print("Loop berhenti pada gos < ", gos)
        break # Menghentikan loop saat gos mencapai 5
    print(gos)
    
#___________________________________________________________________________#

# Penggunaan continue statement untuk melewati iterasi tertentu
print("\n\033[4mContinue Statement\033[0m\n")

for lis in range(1, 6):
    if lis == 3:
        continue  # Melewati angka 3
    print(lis)

#___________________________________________________________________________#

# Penggunaan else dengan for loop
print("\n\033[4mElse Loop\033[0m\n")

for leo in range(1, 6):
    print(leo)
else:
    print("Loop selesai tanpa terhenti dengan break")

#___________________________________________________________________________#

# Penggunaan for loop dengan enumerate
# Enmurate di sini digunakan untuk menampilkan indeks
print("\n\033[4mFor Loop Enumerate\033[0m\n")

hewan = ["apel", "andri", "pisang", "jambu"]
for index, hewan in enumerate(hewan):
    print(f"Indeks {index}: {hewan}")
