# Operasi komparasi

# Setiap hasil dari komparasi adalah boolean

# > , < , <= ,== , != , is ,is not

a = 4
b = 2
# Lebih besar dari
print("\n== Lebih Besar Dari (>)==\n")

hasil = a > b
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b > a
print(b, '>', a, '=', hasil)


# Kurang dari
print("\n== Lebih Kurang Dari (<)==\n")

hasil = a < b
print(a, '<', 3, '=', hasil)
hasil = b < 3
print(b, '<', 3, '=', hasil)
hasil = b < a
print(b, '<', a, '=', hasil)

print("\n== Lebih Besar sama dengan Dari (<=)==\n")

hasil = a <= b
print(a, '<=', 3, '=', hasil)
hasil = b <= 3
print(b, '<=', 3, '=', hasil)
hasil = b <= a
print(b, '<=', a, '=', hasil)

print("\n== Sama Dengan Dari (==)==\n")

hasil = a == b
print(a, '==', 3, '=', hasil)
hasil = b == 3
print(b, '==', 3, '=', hasil)
hasil = b == a
print(b, '==', a, '=', hasil)

print("\n== Tidak Sama Dengan(!=)==\n")

hasil = a != b
print(a, '!=', 3, '=', hasil)
hasil = b != 3
print(b, '!=', 3, '=', hasil)
hasil = b != a
print(b, '!=', a, '=', hasil)


print("\n== is Sebagai komparasi object Identity (is)==\n")

x = 5  # ini adalah assigment membuat object
y = 5

print('Nilai x', x, ',id =', hex(id(x)))
print('Nilai y', y, ',id =', hex(id(y)))
hasil = x is y
print('x is y =', hasil)

print("\n== is Sebagai komparasi object Identity (is not)==\n")

print('Nilai x', x, ',id =', hex(id(x)))
print('Nilai y', y, ',id =', hex(id(y)))
hasil = x is not y
print('x isnot y =', hasil)
