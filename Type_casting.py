print("\033[4mType Casting\033[0m\n")

print("\033[4mInteger ke Float\033[0m\n")
angka_int = 10
angka_float = float(angka_int)
print("Integer ke Float:", angka_float)

print("\033[4mFloat ke Integer\033[0m\n")
angka_float = 12.36
angka_int = int(angka_float)
print("Float ke Integer:", angka_int)

print("\033[4mInteger ke String\033[0m\n")
angka_int = 100
angka_str = str(angka_int)
print("Integer ke String:", angka_str)

print("\033[4mString ke Integer\033[0m\n")
angka_str = "123"
angka_int = int(angka_str)
print("String ke Integer:", angka_int)

print("\033[4mString ke Float\033[0m\n")
angka_str = "56.28"
angka_float = float(angka_str)
print("String ke Float:", angka_float)

print("\033[4mBoolean ke Integer\033[0m\n")
angka_bool = True
angka_int = int(angka_bool)
print("Boolean ke Integer:", angka_int)

print("\033[4mInteger ke Boolean\033[0m\n")
angka_int = 0
angka_bool = bool(angka_int)
print("Integer ke Boolean:", angka_bool)
