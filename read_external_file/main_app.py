# membaca file external dengan open dan with


# 1. membaca file external dengan open

print(3*"=", "membaca file external dengan open", 3*"=")

file = open("data.txt", mode="r")
print(f"status read : {file.readable()}")
print(file.writable())
# print(file.read()) # baca seluruh isi file
#
# print(file.readline(), end="")  # baca baris pertama / baca per baris
# print(file.readline(), end="")  # baca baris kedua
# tanda end="" untuk menghilangkan enter setelah print


# baca file semua baris sebagai list

# print(file.readlines())  # baca isi file sebagai list

# file yang sudah kita buka harus kita close

print(f"apakah file sudah di close : {file.closed}")

# unti=uk menutup file
# file.close()
print(f"apakah file sudah di close : {file.closed}")

# Salah satu teknik membuka file di python dengan with
print("\n", 3*"=", "membaca file external dengan with", 3*"=")

with open("data.txt", mode="r") as file:
    content = file.read()
    print(content, end="")
    print(f"apakah file sudah di close : {file.closed}")
print(f"apakah file sudah di close : {file.closed}")
