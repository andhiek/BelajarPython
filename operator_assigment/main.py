# Operator assignment
# operasi yang dapat di lakukan dengan penyikatan
# operasi ditambah dengan assignment

a = 5  # ini adalah assignment
print("nili a = ", a)

a += 1  # artinya a = a + 1
print("nilai a di += menjadi = ", a)

a -= 2  # artinya a = a - 2
print("nilai a di += menjadi = ", a)

a *= 5  # artinya a = a * 2
print("nilai a di += menjadi = ", a)

a /= 2  # artinya a = a - 2
print("nilai a di += menjadi = ", a)


print('\n=======modulus & floor division=========\n')
b = 10
print("nilai b = ", b)

b %= 3  # artinya b = b % 3
print("nilai b = ", b)

b = 10
print("nilai b = ", b)

b //= 3  # artinya b = b // 3
print("nilai b di //= (division) menjadi = ", b)

print("\n=========pangkat / eksponen===========\n")

a = 5
print('nilai a = ', a)

a **= 3
print('nilai a **= (pangkat) menjadi =  ', a)


# ini adalah operasi bitwise
# OR
print("\n=========operasi bitwise===========\n")
print("OR")
c = True
print('nilai c adalah True', c)

c != False
print('nilai c di != False (tidak sama dengan /OR) menjadi = ', c)

c = False
c != False
print('NIlai c =', c)
print('nilai c di != False(tidak sama dengan /OR) menjadi =  ', c)

# AND
print("AND")

c = True
print('nilai c adalah ', c)

c &= False
print('nilai c di &=(AND) menjadi =', c)

c = True
c &= True
print('nilai c adalah ', c)
print('nilai c &= True menjadi = ', c)
# XOR
print("XOR")

c = True
print('nilai c adalah ', c)

c ^= False
print('nilai c ^= (XOR) False  menjadi ', c)

c = True
print('nilai c', c)
c ^= True
print('nilai c ^= (XOR)True menjadi ', c)

# Shift
print("\n=========operasi SHIFT (geser)===========\n")

d = 0b0100
print('nilai d = ', format(d, '04b'))

d >>= 2
print('nilai d >>= 2 (shift right 2) menjadi = ', format(d, '04b'))

d <<= 1
print('nilai d <<= 1 (shift left 2) menjadi = ', format(d, '04b'))
