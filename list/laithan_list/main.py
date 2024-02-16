# latihan list


# Program List buku
list_buku = []
while True:
    print("Masukan data buku")
    judul = input("masukan judul buku\t:")
    penulis = input("masukan nama penulis\t:")

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)
    print("\n==== Data Buku =====\n")
    print("No\t | Judul\t\t | Penuls")
    for index, buku in enumerate(list_buku):
        print(f"{index+1}\t | {buku[0]}\t\t | {buku[1]} ")
    print("\n==== Akhir Data =====\n")
    islanjut = input("Apakah dilanjutkan  (y/n) ?")
    if islanjut == "n":
        break
    print("PROGRAM SELESAI!!!")
