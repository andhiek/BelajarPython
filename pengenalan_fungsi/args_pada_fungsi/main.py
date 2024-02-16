# Args pada fungsi
import os
os.system('clear')

print("=== Args Pada Fungsi ===")

print("\n=== memasukan data /argument ===")


def fungsi(nama, tinggi, berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")


fungsi("ucup", 170, 40)


def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")


fungsi(["otong", 100, 120])


def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")


fungsi("dudung", 120, 120)

# studi kasus


def tambah(*data):
    output = 0
    for angka in data:
        output += angka

    return output


hasil = tambah(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"hasil = {hasil}")

hasil = tambah(10, 5, 12)
print(f"hasil = {hasil}")


# keyword kwargs
print("\n==== Keyword Kwargs")


def f_kuadrat(angka):
    return angka**2


print(f"hasil angka kuadrat = {f_kuadrat(3)}")


# study kasus

def math(*args, **kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("tidak ada operasi")
    return output


hasil = math(1, 2, 3, 4, 5, 6, option="tambah")
print(f"hasil penjumlhan = {hasil}")
hasil = math(1, 2, 3, 4, 5, 6, option="kali")
print(f"hasil perkalian = {hasil}")


# dengan lamda


def kuadrat(angka): return angka**2


print(f"hasil dari lamda kuadrat = {kuadrat(3)}")


def pangkat(num, pow): return num**pow


print(f"hasil lambda pangkat = {pangkat(4,3)}")


# kegunaannya

# 1 . sorting list
data_list = ["otong", "ucup", "dudung"]
data_list.sort()
print(f"sorting list = {data_list}")


# sorting dia pakai panjang

def panjang_nama(nama):
    return len(nama)


data_list.sort(key=panjang_nama)
print(f"sorted list by panjang = {data_list}")


# sort pakai lamda
data_list = ["otong", "ucup", "Dudung"]
data_list.sort(key=lambda nama: len(nama))
print(f"sorted list by lambda = {data_list}")

# sort by filter
data_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def kurang_dari_lima(angka):
    return angka < 5


data_angka_baru = list(filter(kurang_dari_lima, data_angka))
data_angka_baru = list(filter(lambda x: x < 5, data_angka))
print(data_angka_baru)


# kasus genap
data_genap = list(filter(lambda x: (x % 2 == 0), data_angka))
print(data_genap)

# kasus ganjil
data_ganjil = list(filter(lambda x: (x % 2 != 0), data_angka))
print(data_ganjil)

# kelipatan 3
data_3 = list(filter(lambda x: (x % 3 == 0), data_angka))
print(data_3)

# Anonymous function
print("\n==== Anonymous function ====")

# currying <- haskel curry


def pangkat(angka, n):
    hasil = angka**n
    return hasil


data_hasil = pangkat(5, 2)
print(f"ini adalah fungsi biasa  = {data_hasil}")

# dengan currying


def pangkat(n):
    return lambda angka: angka**n


pangkat2 = pangkat(2)
print(f"pangka 2  = {pangkat2(5)}")
pangkat3 = pangkat(3)
print(f"pangka 3  = {pangkat3(5)}")
print(f"pangkat bebas = {pangkat(4)(5)}")
