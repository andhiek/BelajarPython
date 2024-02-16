# Operasi Logika / Boolean

# Not , And , Or . Xor

# Not
print('\n=====NOT====\n')

a = True
c = not a
print('data a =', a)
print('--------------NOT')
print('data c =', c)


# OR ( jika salah satu true maka hasilnya adalah True)
print('\n=====OR====\n')

a = False
b = False
c = a or b
print(a, "OR", b, "=", c)

a = True
b = False
c = a or b
print(a, "OR", b, "=", c)

a = False
b = True
c = a or b
print(a, "OR", b, "=", c)

a = True
b = True
c = a or b
print(a, "OR", b, "=", c)


# AND (jika salah satu FALSE /keduanya FALSE hasilnya akan FALSE)

print('\n=====AND====\n')

a = False
b = False
c = a and b
print(a, "AND", b, "=", c)

a = True
b = False
c = a and b
print(a, "AND", b, "=", c)

a = False
b = True
c = a and b
print(a, "AND", b, "=", c)

a = True
b = True
c = a and b
print(a, "AND", b, "=", c)


# XOR (jika salah satu TRUE hasilnya akan TRUE sisanya FALSE)
print('\n=====XOR====\n')

a = False
b = False
c = a ^ b
print(a, "XOR", b, "=", c)

a = True
b = False
c = a ^ b
print(a, "XOR", b, "=", c)

a = False
b = True
c = a ^ b
print(a, "XOR", b, "=", c)

a = True
b = True
c = a ^ b
print(a, "XOR", b, "=", c)
