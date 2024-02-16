# Continue and Pass


# pass -> berfungsi sebagai Dummy, tidak akan di eksekusi

# angka = 0

# while angka < 5:
#     angka += 1

#     if angka == 3:
#         print("awaasssss!!!!")
#     print(f"angka = {angka}")


# continue
print("===== Continue ======")

angka = 0

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")

    if angka == 3:
        print("nice")
        continue  # akan membuat loop masuk ke step selanjutnya
    print("lanjut")
print("selesai!!!")
