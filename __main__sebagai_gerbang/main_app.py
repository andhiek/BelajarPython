# __main__ sebagai gerbang program


# __main__ adalah top level code environment

# __main__app pada file program utama

# import package
import package

import fungsi
print(f"nilai name __name__ pada main.py = '{__name__}' ")


# ___name__ pada program external
# import fungsi

# deklarasi
def fungsi_tambah(a: int, b: int) -> int:
    return a+b


# fungsi utama
if __name__ == "__main__":
    angka1 = 5
    angka2 = 10
    hasil = fungsi_tambah(angka1, angka2)
    print(f"hasil tambah = {hasil}")
