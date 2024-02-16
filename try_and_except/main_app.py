# Exception , error ,try anf except


# menghandle error runtime

# study kasus

# data_input = int(input("masukan angka :"))
# hasil = 10/data_input

# print(hasil)

# 1. Exception akan terjadi saat program mengalami error saat runtime

# Contoh sederhana untuk menangkap exception
from math import nan

# input_user = int(input("masukan angka : "))
# hasil = nan
# try:
#     hasil = 10/input_user
# except:
#     print("input tidak boleh 0")
# print(f"hasil = {hasil}")


# contoh pada aplikasi

while (True):
    angka = int(input("masukan angka pembagi : "))
    try:
        hasil = 10/angka
        print(f"hasil = {hasil}")
        is_done = input("lanjutkan (y/n)? ")
        if is_done == "n":
            break
    except:
        print("pembagi nol , silahkan masukan input lagi")
print("akhir dari program 1 terima kasih!!!")


# contoh aplikasi untuk membuat file data.txt
try:
    with open("data.txt", 'r') as file:
        print(file.read())

except:
    print("file data tidak ditemukan, membuat file data.txt")
    with open("data.txt", 'w', encoding='utf-8') as file:
        file.write("file baru berhasil dibuat!")


print("akhir dari program 2")
