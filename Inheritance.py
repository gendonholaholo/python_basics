# Digunakan untuk mewarisi semua metode dan properti kelas lain
# Aturan wajib harus ada KELAS INDUK dan KELAS ANAK

# Kelas Induk
class NamaWanita:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

Lisa = NamaWanita("Elisabeth", "Raditya")
Lisa.printname()


# Kelas anak yang mewarisi segalanya dari induk TANPA tambahan property dan methode apapun
class Anaknya(NamaWanita):
    pass

Leo = Anaknya("Leonardo", "Darmawan")
Leo.printname()


# Kelas anak yang menggunakan konstraktor
class Anaknya:
    def __init__(self, fname, lname): # Pendeklarasian konstraktor akan menggantikan __init__ dari kelas induk
        NamaWanita.__init__(self, fname, lname) # Maka panggil kembali method init di dalam konstraktor child


# Menggunakan fungsi super() untuk mewarisi semua atribut dan method induk (parent)
class Anaknya(NamaWanita):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


# Menambahkan properti & method pada kelas anak
class SiapaItu(NamaWanita):
    def __init__(self, fname, lname, umur):
        super().__init__(fname, lname)
        self.umur = umur
    def halo(self):
        print(f"Halo {self.firstname} {self.lastname}! Sepertinya kamu berumur {self.umur} tahun.")

Orgil = SiapaItu("Orang", "Gila", 27)
Orgil.printname()
Orgil.halo()
