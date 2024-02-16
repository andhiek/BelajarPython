# Fungsi Dengan Argument(input)
import os

os.system('clear')
print("==== FUNGSI DENGAN ARGUMENT ====")


''' def nama_fungsi(argument.parameter/input):
                  -> ini adalah badan fungsi'''


def hello_world(nama):
    ''''fungsi menerima input dengan variabel nama'''
    print(f"Selamat datang dunia wahai {nama}")


hello_world('ucup')
hello_world('asep')


# Program tambah

def tambah(angka_1, angka_2):
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")


tambah(3, 4)
tambah(1000, 10)


def daftar(list_anggota):
    data_anggota = list_anggota.copy()
    for anggota in data_anggota:
        print(f"Yang Terhormat {anggota}")


anggota = ['ucup', 'otong', 'didin']

daftar(anggota)
