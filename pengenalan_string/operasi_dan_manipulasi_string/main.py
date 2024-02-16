# Operasi dan Manipulasi String

# 1. Menyambung string (Concatenane)

nama_pertama = "ucup"
nama_tengah = "D"
nama_akhir = "Fame"

nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)


# 2. Menghitung panjang string

panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. mengecak apakah ada komponen char atau string di string

d = "d"
status = d in nama_lengkap
print("string", d, " ada di " + nama_lengkap + " = " + str(status))
# Hasil False karena d di baca lowercase sedangkan yang di string adalah uppercase

d = "D"
status = d in nama_lengkap
print("string", d, " ada di " + nama_lengkap + " = " + str(status))

d = "d"
status = d not in nama_lengkap
print("string", d, " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)
print(15*"wk")

# 4. Indexing (semua string di mulai dari index ke 0)
# jumlah string ucup = 3 (0,1,2,3)
print("index ke-0 : ", nama_lengkap[0])
print("index ke-1 : ", nama_lengkap[1])
print("index ke-2 : ", nama_lengkap[2])
print("index ke-7 : ", nama_lengkap[7])
print("index ke-(-1) : ", nama_lengkap[-1])
# yang belakang tidak di ambil jika mw ambil kata ucup index harus di tambah 1
print("index ke-[0:4] : ", nama_lengkap[0:4])


# Item paling kecil
print("Paling kecil : " + min(nama_lengkap))
# Item paling Besar
print("Paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah = " + chr(data))

# 4. operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada " + data + " = " + str(jumlah))
