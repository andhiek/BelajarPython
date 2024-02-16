# Operasi pada List

data_angka = [1, 2, 3, 3, 3, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10]

# mencari /menghitung data yang berulang
# count data
jumlah_angka_4 = data_angka.count(4)
jumlah_angka_3 = data_angka.count(3)

print(f"jumlah data angka 4 = {jumlah_angka_4}")
print(f"jumlah data angka 3 = {jumlah_angka_3}")

# ambil posisi data (index)
data = ["ucup", "otong", "dudung", "ujang"]
print(data)
index_dudung = data.index("dudung")
index_ujang = data.index("ujang")
print(f"index data dudung = \n{index_dudung}")
print(f"index data ujang = \n{index_ujang}")

# mengurutkan data / sort
print(f"data list sebelum di sort : {data}")
data_angka.sort()
print(f"data angka sort : \n{data_angka}")
print(f"data : \n{data}")
data.sort()
print(f"data sort : \n{data}")

# membalik urutan list
data_angka.reverse()
print(f"data_angka : \n{data_angka}")
