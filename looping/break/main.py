# Break


data_int = int(input("Hitung sampai : "))

angka = 0
while True:
    angka += 1
    print(f"count = {angka}")

    if angka == data_int:
        print("nice")
        break
    print("Lanjut!!!")
print("selesai!!!!")
