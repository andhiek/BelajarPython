# default argument
import os
os.system('clear')

# def fungsi(argument = nilai defaultnya)
print("\n=== FUNGSI DENGAN DEFAULT ARGUMENT")


def say_hello(nama="Ganteng"):
    '''fungsi dengan default argument'''
    print(f" hello {nama}")


say_hello("ucup")
say_hello()


def sapa_dia(nama, pesan="apa kabar"):
    '''fungsi dengan satu input biasa dan satu input default'''
    print(f"hai {nama} {pesan}")


sapa_dia("dudung")
sapa_dia("otong")


def hitung_pangkat(angka, pangkat=2):
    hasil = angka**pangkat
    return hasil


print(hitung_pangkat(2, 4))

hasil = hitung_pangkat(pangkat=3, angka=3)
print(hasil)


def fungsi(input1=1, input2=2, input3=3, input4=4):
    hasil = input1+input2+input3+input4
    return hasil


print(fungsi())
print(fungsi(input3=10))
