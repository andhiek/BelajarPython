# Persiapan membaut project CRUD
import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print("=========================")

    # Check Databases
    CRUD.init_console()

    while (True):
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")
        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN")
        print("=========================")

        print("1. Read Data")
        print("2. Create Data")
        print("3. Updata Data")
        print("4. Delete Data")

        user_option = input("Masukan Opsi: ")

        match user_option:
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": CRUD.delete_console()
        is_done = input("Apakah Selesai (Y/N) ?")
        if is_done == "y" or is_done == "Y":
            break

    print("Program Berakhir,Terima Kasih !")
