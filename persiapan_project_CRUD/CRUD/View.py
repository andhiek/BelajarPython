# Read console
from . import Operasi


# Fungsi Delete view
def delete_console():
    read_console()
    while (True):
        print("Silahkan pilih no buku yang akan di Hapus / Delete: ")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            data_break = data_buku.split(',')
            pk = data_break[0]
            data_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]

            # Data yang ingin di update
            print("\n"+"="*100)
            print("Data Buku yang akan di Hapus!")
            print(f"1. Judul\t:{judul:.40}")
            print(f"2. Penulis\t:{penulis:.40}")
            print(f"3. Tahun\t:{tahun:4}")

            is_done = input("Apakah anda yakin  menghapus data ini (Y/N) ?")
        if is_done == "y" or is_done == "Y":
            Operasi.delete(no_buku)
            break

        else:
            print("No buku tidak di hapus!!")
            break
    print("Data Berhasil di Hapus!!")


# Fungsi view Update
def update_console():
    read_console()
    while (True):
        print("Silahkan pilih no buku yang akan di Update: ")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            break
        else:
            print("No buku tidak valid, Silahkan masukan lagi!!")

    data_break = data_buku.split(',')
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    while (True):
        # Data yang ingin di update
        print("\n"+"="*100)
        print("Silahkan pilih data yang akan di ubah!")
        print(f"1. Judul\t:{judul:.40}")
        print(f"2. Penulis\t:{penulis:.40}")
        print(f"3. Tahun\t:{tahun:4}")

        # memilih mode untuk update
        user_option = input("Pilih data [1,2,3]: ")
        print("\n"+"="*100)
        match user_option:
            case "1": judul = input("judul\t:")
            case "2": penulis = input("penulis\t:")
            case "3":
                while (True):
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print(
                                "tahun harus angka,  silahkan masukan angka tahun (yyyy)")

                    except:
                        print(
                            "tahun harus angka,  silahkan masukan angka tahun (yyyy)")
            case _: print("Index yang anda pilih tidak ada!!")

        print("Data Baru anda!!!")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        is_done = input("Apakah data sudah sesuai (Y/N) ?")
        if is_done == "y" or is_done == "Y":
            break

    Operasi.update(no_buku, pk, data_add, tahun, judul, penulis)


# Fungsi Create view
def create_console():
    print("\n\n"+"="*100)
    print("Silahkan Tambah Data buku\n")
    penulis = input("Penulis\t: ")
    judul = input("Judul\t: ")
    while (True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("tahun harus angka,  silahkan masukan angka tahun (yyyy)")

        except:
            print("tahun harus angka,  silahkan masukan angka tahun (yyyy)")

    Operasi.create(tahun, judul, penulis)
    print("\nberikut adalah data baru anda:")
    read_console()


# Fungsi Read view
def read_console():
    data_file = Operasi.read()
    index = "No"
    judul = "judul"
    penulis = "penulis"
    tahun = "tahun"


# Header
    print("\n"+"="*100)
    print(f"{index:4}| {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)


# Data
    for index, data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        data_add = data_break[1]
        judul = data_break[2]
        penulis = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4}| {judul:.40} | {penulis:.40} | {tahun:4}", end="")


# Footer
    print("="*100+"\n")
