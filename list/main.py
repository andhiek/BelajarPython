# List

# Kumpulan data numbers
print("\n==== Data Numbers ====")
data_angka = [1, 2, 3]
print(data_angka)

# Kumpulan data string
print("\n==== Data String ====")

data_nama = ["andi", "ucup", "otong", "firman"]
print(data_nama)

# Kumpulan data boolean
print("\n==== Data Boolean ====")
data_bool = [True, False, True, True]
print(data_bool)


# Kumpulan data campuran
print("\n==== Data Campuran ====")
data_campuran = [True, "andi", 1, 2, 3, 4, False, "ucup"]
print(data_campuran)


# cara alternatif membuat list
print("\n==== Data Range ====")
data_range = range(0, 10, 2)  # range( start ,stop ,step)
print(data_range)
data_list = list(data_range)
print(data_list)


# membuat list dengan loop, list comperehension
print("\n==== List pake for ====")
list_pake_for = [i for i in range(0, 10)]
print(list_pake_for)

list_pake_for = [i**2 for i in range(0, 10)]
print(list_pake_for)

# membuat list pakek for if
print("\n==== List pake for ====")
list_pake_for_if = [i for i in range(0, 10) if i != 5]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0, 10) if i % 2 == 0]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0, 10) if i % 2 == 1]
print(list_pake_for_if)
