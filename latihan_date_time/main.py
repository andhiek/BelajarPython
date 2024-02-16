# Latihan Date And Time

import datetime as dt
hari_ini = dt.date.today()


print("Silahkan masukan tanggal ,bulan,tahun,lahir anda :")
tanggal = int(input("tanggal \t: "))
bulan = int(input("bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"tanggal lahir anda adalah :  {tanggal_lahir}")
print(f"hari kelahiran anda hari {tanggal_lahir:%A}")
hari_ini = dt.date.today()
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365) // 30
print(f"umur anda adalah : {umur_tahun} tahun {umur_bulan} bulan")
