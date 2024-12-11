from karyawan import Karyawan

class Perusahaan:
    def __init__(self, nama_perusahaan):
        self.nama_perusahaan = nama_perusahaan
        self.total_karyawan = []

    def tambah_karyawan(self, karyawan):
        if isinstance(karyawan, Karyawan):
            self.total_karyawan.append(karyawan)
        else:
            raise ValueError("Hanya objek Karyawan yang bisa ditambahkan.")

    def tunjukan_karyawan(self):
        for krywn in self.total_karyawan:
            print(krywn)

if __name__ == "__main__":
    krywn1 = Karyawan(2843701, "Gos")
    krywn2 = Karyawan(2843702, "Lisa")

    perusahaan = Perusahaan("Keluarga")
    perusahaan.tambah_karyawan(krywn1)
    perusahaan.tambah_karyawan(krywn2)

    perusahaan.tunjukan_karyawan()

    print(f"ID Karyawan 1: {krywn1.id_karyawan}")
    print(f"ID Karyawan 2: {krywn2.id_karyawan}")

    try:
        krywn1.id_karyawan = 9999
    except ValueError as e:
        print(f"Error: {e}")
