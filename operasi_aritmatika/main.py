# Operasi Aritmatika
'''
1.()
2.Eksponen
3.Perkalian dan temen-teman * / ** % //
4.Pertambahan dan pengurangan + -
5. NB: Angka yang di dalam kurung akan di eksekusi duluan
'''


a = 10
b = 3

# Operasi Pertambahan

hasil = a + b
print(a, "+", b, "=", hasil)

# Operasi Pengurangan
hasil = a - b
print(a, "-", b, "=", hasil)

# Operasi Perkalian
hasil = a * b

print(a, "*", b, "=", hasil)

# Operasi Pembagian /

hasil = a / b
print(a, "/", b, "=", hasil)

# Operasi Eksponen (Perpangkatan)

hasil = a ** b
print(a, "**", b, "=", hasil)

# Operasi MOdulus %

hasil = a % b
print(a, "%", b, "=", hasil)

# Operasi Division //
hasil = a // b
print(a, "//", b, "=", hasil)

# Prioritas Operasi , Operasi precedence
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x, '**', y, '*', z, '+', x, '/', y, '-', y, '%', z, '//', x, '=', hasil)
# kurung akan di eksekusi duluan
