# ELIF = ELSE IF STATEMENT

nama = input("Masukan nama:")

# if kondisi:
#     aksi True
# elif kondisi
#     aksi True
# else
#     aksi


if nama == "ucup":  # kondisi 1
    print(f"Selamat datang {nama}")  # akhir True 1
elif nama == "otong":  # kondisi 2
    print(f"selamat datang {nama}")  # aksi True 2

elif nama == "andhi":
    print(f"Hai {nama} selamat datang! ")  # aksi True 3

else:
    print("nama tidak nama di kenal")  # aksi False


print("ini akhir dari program,,Trima kasih!!")
