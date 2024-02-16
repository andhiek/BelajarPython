# Latihan Fungsi

import os
print("\n=== latihan fungsi ==== \n")


# Program menghitung luas dan keliling persegi panjang

# 1 Membuat header Program
# os.system('clear')

# print(f"{'PROGRAM  MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# # mengambil input user
# LEBAR = int(input("Masukan nilai lebar  : "))
# PANJANG = int(input("Masukan nilai panjang : "))

# # Program menghitung luas
# LUAS = PANJANG * LEBAR
# KELILING = 2*(PANJANG+LEBAR)

# # Tampilkan hasilnya
# print(f"Hasil perhitungan  luas = {LUAS}")
# print(f"Hasil perhitungan  keliling = {KELILING}")


# Dengan menggunakan fungsi

# membuat header

def header():
    '''fungsi header'''
    os.system('clear')
    print(f"{'PROGRAM  MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

# mengambil input user


def inputUser():
    '''fungsi input user'''
    lebar = int(input("Masukan nilai lebar  : "))
    panjang = int(input("Masukan nilai panjang : "))

    return lebar, panjang

# menghitung luas


def hitung_luas(lebar, panjang):
    '''fungsi hitung luas'''
    return lebar * panjang


def hitung_keliling(lebar, panjang):
    '''fungsi hitung keliling'''
    return 2*(lebar+panjang)


def display(message, value):
    '''fungsi display'''
    print(f"Hasil perhitungan {message} {value}")


# main program
while True:
    header()
    LEBAR, PANJANG = inputUser()
    LUAS = hitung_luas(LEBAR, PANJANG)
    KELILING = hitung_keliling(LEBAR, PANJANG)

    display("luas = ", LUAS)
    display("keliling", KELILING)

    isContinue = input(f"Apakah Lanjut (y/n) ? ")
    if isContinue == "n":
        break
print("Program Selesai,Terima kasih!!!")
