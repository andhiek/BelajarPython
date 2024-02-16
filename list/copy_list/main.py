# Copy List

# teknik menduplikat list

a = ["ucup", "otong", "dudung"]
print(f"a : {a}")

b = a  # pass by reference
print(f"b : {b}")

# kita akan merubah member dari a
# akan merubah dari keduanya
a[1] = "michael"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# addrees dari keduanya
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# menduplikat list dengan copy()
c = a.copy()  # Full duplikat

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 0")

c[0] = "dadang"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
