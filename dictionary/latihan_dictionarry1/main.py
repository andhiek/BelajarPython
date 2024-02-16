# Latihan Dictionary

import datetime
import os
import string
import random

print("\n===== Latihan Dictionary 1 ====")

# Template Dict mahasisw
mahasiswa_temp = {
    'nama': 'nama',
    'nim': "nim",
    'sks_lulus': 0,
    'lahir': datetime.datetime(1111, 1, 11)
}
data_mahasiswa = {}


while True:

    os.system('clear')

    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)

    mahasiswa = dict.fromkeys(mahasiswa_temp.keys())

    mahasiswa['nama'] = input("Nama mahasiswa:")
    mahasiswa['nim'] = input("Nim mahasiswa:")
    mahasiswa['sks_lulus'] = int(input("sks lulus mahasiswa:"))
    TAHUN_LAHIR = int(input("tahun lahir (YYYY): "))
    BULAN_LAHIR = int(input("bulan lahir (1-12): "))
    TANGGAL_LAHIR = int(input("tanggal lahir (1-31): "))
    mahasiswa['lahir'] = datetime.datetime(
        TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

    KEY = ''.join(random.choice(string.ascii_uppercase) for i in range(6))
    data_mahasiswa.update({KEY: mahasiswa})

    print(
        f"\n{'KEY':<6} {'Nama':<17} {'NIm':<8} {'SKS LULUS':<10} {'Tanggal Lahir':<10}")
    print('_'*50)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa

        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

        print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {LAHIR:^10}")
    print('\n')
    is_done = input("Tambahkan data mahasiswa (y/n) ?")
    if is_done == 'n':
        break

print("\n Program Selesai!!!")
