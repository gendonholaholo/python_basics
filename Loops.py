# Iterasi dari list (for loop)
print("For Loop\n")

buah = ["apel", "jeruk", "pisang", "mangga"]
for buah in buah:
    print(buah) # Menampilkan setial elemen dalam list 'buah'

for x in range(1, 5):
    print(x) # Menampilkan angka dari satu sampai 4

print("__\n")

#___________________________________________________________________________#

# Penggunaan dalam kondisi tertentu (while loop)
print("While Loop\n")

menghitung = 1
while menghitung <= 5:
    print(menghitung) # Menampilkan dari 1-5
    menghitung += 1

angka = 0
while angka != -1:
    angka = int(input("Masukan angka (-1 untuk berhenti): "))
    print(f"Angka yang dimasukkan: {angka}")

print("__\n")

#___________________________________________________________________________#

# Mencetak tabel perkalian (nested loop)
print("Nested Loop\n")

for i in range(1, 4): # Perulangan baris (1-3)
    for j in range (1, 4): # Perulangan kolom (1-3)
       print(f"{i} x {j} = {i*j}", end="\t")
    print() # Berpindah baris saat satu baris selesai diproses
    
