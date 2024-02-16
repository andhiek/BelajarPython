# Latihan Looping

# Membuat Segitiga

sisi = 10
# 1. Dengan menggunakan For


# dummy variable
print("\n==== awal dari for ====")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1
print("==== akhir dari for ====\n")


# 2. Dengan menggunakan While
print("==== awal dari while ====")

count = 1

while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

print("==== akhir dari while ====\n")

# 3. Ambil ganjil

print("==== ganjil ====")

count = 1
while True:
  # akan kembali ke atas jika ganjil
    if (count % 2):
      # print jika ganjil
        print("*"*count)
        count += 1
    else:  # akan kembali ke atas jika genap
        count += 1
        continue
  # akan break jika count melebihi sisi
    if count > sisi:
        break

print("==== akhir ganjil ====")


# 4. tambah spasi di depan segitiga

print("==== geser segitiga ====")

count = 1
spasi = int(sisi/2)
while True:
  # akan kembali ke atas jika ganjil
    if (count % 2):
      # print jika ganjil
        print(" "*spasi, "+"*count)
        spasi -= 1
        count += 1
    else:  # akan kembali ke atas jika genap
        count += 1
        continue
  # akan break jika count melebihi sisi
    if count > sisi:
        break

print("==== geser segitiga ====\n")

# membuat ketupat
print("==== ketupat versi AI ====")


def print_ketupat(rows):
    # Bagian atas segitiga ketupat
    for i in range(1, rows + 1):
        for j in range(1, rows - i + 1):
            print(" ", end="")
        for k in range(1, i * 2):
            print("*", end="")
        print()

    # Bagian bawah segitiga ketupat
    for i in range(rows - 1, 0, -1):
        for j in range(1, rows - i + 1):
            print(" ", end="")
        for k in range(1, i * 2):
            print("*", end="")
        print()


# Input jumlah baris
num_rows = int(input("Masukkan jumlah baris: "))

print_ketupat(num_rows)
print("==== akhir ketupat ====\n")


print("==== ketupat  ====")

user_input = int(input("masukan angka: "))
count = 1
spasi = user_input // 2
while True:
    if count > user_input:
        break
    elif count % 2 == 0:
        count += 1
        spasi -= 1
        continue
    print(" "*spasi + "*"*count)
    count += 1

angka = count - 1
while True:
    if angka == 0:
        break
    elif angka % 2 == 0:
        angka -= 1
        spasi += 1
        continue
    print(" "*spasi + "*"*angka)
    angka -= 1
    count += 1
print("==== ketupat akhir ====")
