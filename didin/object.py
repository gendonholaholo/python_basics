class namaWanita:
    namaSaya = "Nama saya Lisa."

elisa = namaWanita()

print(elisa.namaSaya)

# -------------------------------

class namaPria:
    def __init__(self, nama, umur, pekerjaan):
        self.nama = nama
        self.umur = umur
        self.pekerjaan = pekerjaan

gos = namaPria("Gos", 26, "Nganggur")
print(f"Nama saya adalah {gos.nama}, saya berumur {gos.umur} dan saya bekerja sebagai {gos.pekerjaan}.")

# -------------------------------

class namaAnak:
    def __init__(self, nama, umur, hobi):
        self.nama = nama
        self.umur = umur
        self.hobi = hobi

    def __str__(self):
        return f"{self.nama} ({self.umur} ({self.hobi}))"

leo = namaAnak("Leo", 7, "Nitendo")
print(f"Namaku {leo.nama}, umurku {leo.umur}, aku suka sekali bermain {leo.hobi}.")

# ----------------------------

# Memodifikasi nilai dari atribut di dalam object
gos.nama = "Ghaws"
leo.hobi = "sama mamah"

print(f"Nama saya adalah {gos.nama}, saya berumur {gos.umur} dan saya bekerja sebagai {gos.pekerjaan}.")
print(f"Namaku {leo.nama}, umurku {leo.umur}, aku suka sekali bermain {leo.hobi}.")


