# Setter getter digunakan untuk memberikan aturan pada sebuah atribut
# Analogi. Lisa punya lemari & lemari itu tidak boleh diakses sembarang orang dan juga memasukan barang di dalamnya pun ada aturannya. Di dalam lemari tersebut berisi surat yang hanya ditujukan kepada Lisa, buku harian, dan pakaian dalam.
# Setiap Lisa mendapatkan surat diakan selalu melakukan cek pada surat itu apakah surat itu ditujukan pada dia atau tidak dan jika iya maka akan dimasukan ke dalam lemari (aturan ini adalah sebuah validasi yang nanti akan kita gunakan di dalam setter)
# Tentunya lemari ini hanya bisa diakses oleh Lisa dengan kunci tertentu, maka ketetapan validasi di dalam setter tersebutlah kuncinya
# Lantas bagaimana cara kita memasukan kuncinya? Kita harus tau dulu di mana letak lubang kuncinya; ini lah yang disebut getter
# Setelah setter (aturan validasi) dibuat dan getter (lubang kunci) ditemukan, baru kita implementasikan atribut itu dengan semestinya

# Contoh object biasa dengan validasi langsung (tanpa setter getter)
class NamaWanita:
    def __init__(self, nama, umur):
        self._nama = nama
        self._umur = umur
    
    def get_nama(self):
        return self._nama

    def set_nama(self, value):
        if len(value) <= 3:
            print("Nama tidak valid. Harus lebih dari 3 huruf.")
        else:
            self._nama = value

if __name__ == "__main__":
    wanita = NamaWanita("Elisa", 26)
    print(wanita.get_nama())
