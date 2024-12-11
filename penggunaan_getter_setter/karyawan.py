class Karyawan:
    def __init__(self, id_karyawan, name):
        self._id_karyawan = id_karyawan
        self.name = name

    @property
    def id_karyawan(self):
        return self._id_karyawan

    @id_karyawan.setter
    def id_karyawan(self, value):
        raise ValueError("ID karyawan tidak bisa diubah setelah objek dibuat.")

    def __str__(self):
        return f"ID Karyawan: {self.id_karyawan}, Nama: {self.name}"
