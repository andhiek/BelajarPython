# fungsi dengan return
import os
os.system('clear')
print("\n==== FUNGSI DENGAN RETURN ==== ")


# fungsi kuadrat

def kuadrat(input_angka):
    output_kuadrat = input_angka**2
    return output_kuadrat


y = kuadrat(3)
print(y)

print(kuadrat(6))


z = 10 + kuadrat(7)
print(z)


# fungsi tambah

def fungsi_tambah(angka_1, angka_2):
    return angka_1 + angka_2


a = fungsi_tambah(10, 5)
print(a)

# Fungsi dengan return banyak


def operasi_matematika(angka_1, angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2

    return tambah, kurang, kali, bagi


k, l, m, n = operasi_matematika(9, 5)

print(f"hasil tambah 9 + 5 = {k}")
print(f"hasil kurang 9 - 5 = {l}")
print(f"hasil kali   9 * 5 = {m}")
print(f"hasil bagi   9 / 5 = {n}")
