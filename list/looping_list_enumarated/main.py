# loping list enumarated

# looping dari list

# mggunakan for loop
print("\n=== for loop ====")
kumpulan_angka = [4, 3, 2, 5, 6, 1]
for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["ucup", "otong", "dadang", "dina"]

for nama in peserta:
    print(f" nama peserta : {nama}")

# for loop dan range
print("\n=== for loop dan range ====")

kumpulan_angka = [10, 5, 4, 3, 2, 1]

panjang = len(kumpulan_angka)
for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")


# while
print("\n=== While loop ====")


kumpulan_angka = [10, 5, 4, 3, 2, 1]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1


# List comprehension
print("\n=== List comprehension ====")

data = ["ucup", 1, 2, 3, "otong"]
[print(f"data = {i}") for i in data]

angka = [10, 5, 4, 3, 2, 1]
angka_kuadrat = [i**2 for i in angka]
print(f"angka = {angka_kuadrat}")


# enumarated (akan mengambil data dan index)
print("\n=== Enumarated ====")


data_List = ["ucup", 1, 2, 3, "otong"]

for index, data in enumerate(data_List):
    print(f"data = {index}, data = {data}")
