# Nested List


data_0 = [1, 2]
data_1 = [3, 4]
data_list_biasa = [1, 2, 3, 4]
print("\n=== data biasa ===")
print(f"List biasa = {data_list_biasa}")

list_2D = [data_0, data_1]
print(f"list 2D = {list_2D}")

# contoh penggunakan nested list

peserta_0 = ["ucup", 25, "Laki-laki"]
peserta_1 = ["otong", 27, "Laki-laki"]
peserta_2 = ["dian", 21, "Wanita"]

list_peserta = [peserta_0, peserta_1, peserta_2]

print("\n==== nested list ====")
print(f" daftar peserta : {list_peserta}")

for peserta in list_peserta:
    print(f"nama\t:{peserta[0]}")
    print(f"umur\t:{peserta[1]}")
    print(f"gender\t:{peserta[2]}\n")

# Deep copy nested list

print("==== Deep copy nested list ====\n")

# mengambil data dari nested list

data_0 = [1, 2]
data_1 = [3, 4]

data_2D = [data_0, data_1]

data = data_2D[0][0]
print(f"data_2D : {data_2D}")
print(f"data = {data}")
