# Mendifinisikan fungsi
def say_hello():
    print("Hallo Lisa")

def jumlah(z,f):
    return z+f

def sapa(nama):
    print("Hello, " + str(nama))
    # print(f"Hello, {nama}")

def add(a,b):
    return a+b
result = add(3,5)

# Menjalankan fungsi dan menerima dua nilai yang dikembalikan
_namaDepan, _namaBelakang = get_full_name("Leonardo", "Darmawan")

print(f"Nama lengkap: {_namaDepan} {_namaBelakang}")

