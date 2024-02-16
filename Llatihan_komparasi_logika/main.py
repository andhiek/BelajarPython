# Latihan KOmaprasi Dan Logika

#  Membuat Gabungan Rentang Area dari Angka


# Latihan satu
# +++++++3--------10+++++++

print("\n====Latihaan 1 =====\n ")
inputUser = float(input(
    "Masukan angka yang bernilai \nkurang dari 3 \natau \nlebih besar dari 10 : "))

# +++++3-------
# Memeriksa angka kurang dari 3

isKurangDari = (inputUser < 3)
print(inputUser, "Kurang dati 3 =", isKurangDari)

# -----10++++
# Memerikas angka lebih dari 10
isLebihDari = (inputUser > 10)
print(inputUser, "Lebih dari 10 = ", isLebihDari)

# gabungan dari rentang area
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan: ", isCorrect)


print("\n====Latihaan 2 =====\n")

# Latihan dua
# irisan

# -------3++++++++10--------
inputUser = float(input(
    "Masukan angka yang bernilai \nlebih  dari 3 \ndan \nkurang dari 10 : "))

# -------3++++++
# memeriksa angak lebih dari 3
isLebihDari = (inputUser > 3)
print(inputUser, "Lebih dari 3 =", isLebihDari)

# +++++++10------
# memeriksa angak kurang  dari 10
isKurangDari = (inputUser < 10)
print(inputUser, "Kurang dari 10 = ", isKurangDari)

isCorrect = isLebihDari and isKurangDari
print("angka yang anda masukan: ", isCorrect)

# Buat Angka
# soal nomor satu
print("\n==== soal nomor satu =======\n")
# --------0++++++++5-------8++++++11----
inputUser = float(
    input("Masukan angka lebih dari 0 \n dan kurang dari 5\n dan \n lebih dari 8 \n kurang dari 11 :"))
# memeriksa angka lebih dari 0
isLebihDari0 = (inputUser > 0)
print(inputUser, "Lebih dari 0 =", isLebihDari0)
# memeriksa angka kurang dari 5
isKurangDari5 = (inputUser < 5)
print(inputUser, "Kurang dari 5 = ", isKurangDari5)
# memeriksa angka kurang dari 8
isLebihDari8 = (inputUser > 8)
print(inputUser, "Kurang dari 8 = ", isLebihDari8)
# memeriksa angka kurang dari 11
isKurangDari11 = (inputUser < 11)
print(inputUser, "Kurang dari 11 = ", isKurangDari11)

# Menggabungka hasil
isCorrect = isLebihDari0 and isKurangDari5 or isLebihDari8 and isKurangDari11
print("Angka yang anda masukan: ", isCorrect)


print("\n==== soal nomor dua ========\n")
# +++++++0-------5 ++++++ 8 -------- 11 ++++++++
inputUser = float(input(
    "Masukan angka kuranG dari 0 \ndan lebih dari 5 \n atau kurang dari 8 dan lebih dari 11 :"))
# memeriksa angka kurang dari 0
isKurangDari0 = (inputUser < 0)
print(inputUser, "kurang dari 0 = ", isKurangDari0)

# memeriksa angka lebih dari 5
isLebihDari5 = (inputUser > 5)
print(inputUser, "lebih dari 5 = ", isLebihDari5)

# memeriksa angka kurang dari 8
isKurangDari8 = (inputUser < 8)
print(inputUser, " kurang dari 8 = ", isKurangDari8)
# memeriksa angka lebih dari 11
isLebihDari11 = (inputUser > 11)
print(inputUser, "lebih dari 11 = ", isLebihDari11)

# menggabungkan hasil
isCorrect = isLebihDari0 and isKurangDari5 or isKurangDari8 and isKurangDari11
print("angka yang anda masukan = ", isCorrect)
