# --Manipulasi List

# Operasi

# mengambil data dari list
print("\n=== dengan menggunakan index ===")
data = ["andi", "ucup", "otong"]
print(data)
data_0 = data[0]
print(f"idi adalah index ke 0 : {data_0}")
data_terakhir = data[-1]
print(f"ini adalah data -1 : {data_terakhir}")

# mengambil info jumlah data
panjang_data = len(data)
print(f"panjanf data adalah : {panjang_data}")


# menambahkan / memasukan item pada data sesuai posisi
print(f"data sebelum di tambah : \n{data}")
data.insert(1, "asep")
print(f"data setelah di tambah: \n{data}")

# menambah item di akhir data list
data.append("Dadang")
print(f"menambah data terakhir : \n{data}")


# menggabung / menambah list dengan list
data_baru = ["Ujang", "firman", "bondan"]
data.extend(data_baru)
print(f"data yang telah di gabung : \n{data}")

# Merubah data
data[1] = "akang"
print(f"data yang telah dirubah : \n{data}")

# menghapus list data
data.remove("Ujang")
print(f"data remove : \n{data}")

# meremove data palng akhir
data_akhir = data.pop()
print(f"hapus data terakhir : \n{data}")
