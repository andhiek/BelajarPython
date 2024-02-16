# Fomat string

# contoh generic
# string
nama = "marlene"
format_str = f"hello {nama}"
print(format_str)

# boolean

boolean = True
format_str = f"boolean = {boolean}"
print(format_str)


print("\n====== angka =====\n")

angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

print("\n====== bilangan bulat =====\n")
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

print("\n====== bilangan dengan ordo ribuan =====\n")
angka = 2000
format_str = f"bilangan ribuan = {angka:,}"
print(format_str)

print("\n====== bilangan decimal =====\n")

angka = 2005.54321
format_str = f"decimal = {angka:.2f}"
print(format_str)

print("\n====== menamppilkan leading zero =====\n")
angka = 2005.54321
format_str = f"leading zero = {angka:010.3f}"
print(format_str)

print("\n====== menamppilkan tanda(+) / (-) =====\n")
angka_minus = -10
angka_plus = 10
format_minus = f"minus = {angka_minus:-d}"
format_plus = f"plus = {angka_plus:+d}"
print(format_minus)
print(format_plus)


print("\n====== memformat persen =====\n")
persentase = 0.045
format_persen = f"persenatse = {persentase:.2%}"
print(format_persen)

print("\n====== membuat operasi aritmatika di dalam {} =====\n")

harga = 10000
jumlah = 5

format_string = f"jumlah = Rp. {harga * jumlah:,}"
print(format_string)

print("\n====== format angka lain (binary,octal,hexadecimal) =====\n")

angka = 253
format_binary = f'binary = {bin(angka)}'
format_octal = f'octal = {oct(angka)}'
format_hex = f'hexadecimal = {hex(angka)}'

print(format_binary)
print(format_octal)
print(format_hex)
