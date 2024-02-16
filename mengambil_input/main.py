# Mengambil Input Dari User

# Data yang dimasukan pasti String
data = input("Masukan Data:")

print("data = ", data, ",type =", type((data)))

# Jika kita ingin mengambil int ,maka
angka = float(input("masukan angka:"))
angka = int(input("masukan angka:"))

print("data = ", angka, ",type =", type((angka)))


# Cara mengambil data boolean ( kita harus casting dulu ke interger baru ke boolean)

biner = bool(int(input("masukan nilai boolean:")))
print("data = ", biner, ",type =", type(biner))
