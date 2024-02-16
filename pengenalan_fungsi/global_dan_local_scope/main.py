# Global dan local scope

print("=== Global dan local scope ====")

# variable global
nama_global = "otong"  # ini aalah variable global


def fungsi():
    print(f"fungsi menampilkan {nama_global}")


fungsi()

# akses variablel global dengan loop

for i in range(0, 5):
    print(f"loop {i} - {nama_global}")

# variable local scope


def fungsi():
    nama_local = "Ucup"


fungsi()

# Contoh 1 : Penggunaan


def say_otong():
    print(f"hello {nama}")


nama = "Otong"
say_otong()

# contoh 2: merubah variable global
angka = 0


def ubah(nilai_baru, nama_baru):
    global angka  # fungsi ini dapat akses ubah angka
    global name
    angka = nilai_baru
    name = nama_baru


print(f"sebelum {angka,nama}")
ubah(10, "Ucup")
print(f"sesudah {angka,name}")


# contoh 3

angka = 0
for i in range(0, 5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 5
    angka_dummy = 10


print(angka)
print(angka_dummy)
