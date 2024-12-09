# Semua yang ada di dalam Python adalah OBJECT karena Python adalah OOP. Method adalah object dari class, fugsi adalah object dari function, dan class pun adalah object dari class `type`

# Contoh object sederhana; dalam implementasinya ini tidak akan pernah digunakan.

# Membuat kelas sebagai blueprint dari object yang nanti dibuat.
class namaWanita:
    namaSaya = "Nama saya Lisa."

# Membuat object
elisa = namaWanita()

print(elisa.namaSaya)
# ------------------------------------------------------------ #


# Ini adalah bentuk umum pendeklarasian kelas untuk object dan akan sering digunakan.
class namaPria():
    def __init__(self, nama, umur, pekerjaan):
        self.nama = nama
        self.umur = umur
        self.pekerjaan = pekerjaan

gos = namaPria("Gos", 26, "Gigolo")

print(f"Nama saya adalah {gos.nama}, saya berumur {gos.umur} dan saya bekerja sebagai {gos.pekerjaan}.")
# ------------------------------------------------------------ #


# Menggunakan fungsi __str__ untuk menkonfigurasi aturan yang nantinya akan mengembalikan dalam bentuk string. 
class namaAnak():
    def __init__(self, nama, umur, hobi):
        self.nama = nama
        self.umur = umur
        self.hobi = hobi

    def __str__(self):
        return f"{self.nama} ({self.umur}) ({self.hobi})" # Penggunaan tanda kurung adalah kebutuhan design. Digunakan untuk merepresentasikan bahwasanya properti itu berkaitan dengan properti pertama

leo = namaAnak("Leo", 7, "Nitendo")

print(f"Namaku {leo.nama}, umurku {leo.umur}, aku suka sekali bermain {leo.hobi}.")

