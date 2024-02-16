# Operator dalam bentuk method

# merubah case dari string

print("====== merubah semua ke uppercase ======")
salam = "bro"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

print("====== merubah semua ke lowercase ======")

alay = "Aku Kece Abiiezzzz"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)


# pengecekan dengan isx method
# contoh untuk pengecekan lower case
salam = "sist"
apakah_lower = salam.islower()  # hasilnya akan boolean
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek apakah semuanya huruf
# isalnum() <--- untuk mengecek apakah huruf dan angka
# isdecimal() <--- untuk mengecek apakah angka saja
# isspace()  <-- untuk mengecek apakah spasi ,newline,tab atau enter
# istitle() <-- untuk mengecek apakah semua kata di mulai dengan huruf besar

# istitle
judul = "It Is Ok Not To Be Orkay"
cek_judul = judul.istitle()  # hasilnya boolean
print(judul + " is title  = " + str(cek_judul))


# mengecek komponen startswith() dan endswith()
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim Oppa")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppa".endswith("Sangjangnim Oppa")
print("end = " + str(cek_end))

# penggabungan komponen join() menggabunkan
# dan split() memisahkan

pisah = ['aku', 'sayang', 'kamu']  # ini adalah list
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'))

# alokasi karakter rjust() , ljust() , center()

kanan = "kanan".rjust(10)
print("'" + kanan + "'")

kiri = "kiri".ljust(10, "-")
print("'" + kiri + "'")

tengah = "tengah".center(10, ":")
print("'" + tengah + "'")

# kebalikannya  -> strip()
tengah = "tengah".strip(":")  # menghilangkan tanda :
print("'" + tengah + "'")
