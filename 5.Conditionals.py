# Input dari pengguna
umur = int(input("Masukan umur: "))

# Menggunakan if-elif-else untuk menentukan kategori umur
if umur < 13:
    print("Anda masih anak-anak.")
elif umur >= 13 and umur < 18:
    print("Anda remaja.")
else:
    print("Mungkin Anda masih kuliah? y/n")
    jawaban = str(input(""))
    if jawaban == "y":
        semester = int(input("Masukan semester: "))
        # Ternary (menulis if else dalam satu baris)
        k_mahasiswa = "Anda mahasiswa bodoh." if semester > 6 else "Anda bukan mahasiswa bodoh."
        print(k_mahasiswa)
    else:
        print("Mungin Anda lansia.")