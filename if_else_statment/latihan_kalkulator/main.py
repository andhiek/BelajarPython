# Latihan Kalkulator sederhana


print(20*"=")
print("Kalkulator Sederhana")
print(20*"="+"\n")


angka_1 = float(input("masukan angka 1 = "))
operator = input("operator (+,-,*,/) = ")
angka_2 = float(input("Masukan angka ke 2 = "))


# percabanganmya

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "*":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil}")
else:
    print("hasil tidak terbaca!!!")
    print("operator yang anda masukan salah!!")

print("Terima kasih telah mencoba program kami!")
