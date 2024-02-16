# Type Pada Fungsi
import string
import os
os.system('clear')
print("==== Type Pada Fungsi ====")

# Bentuk Standar Fungsi
# Studi kasus
'''
print('\n### Bentuk Standart Fungsi ###')


def fungsi(parameter):
    print(parameter)


print(1)
'''
# menggunakan type hints

print('\n@ menggunakan type hints ')


def sepuluh_pangkat(argument: int) -> int:
    '''fungsi dengan hints'''
    output = 10**argument
    return output


HASIL = sepuluh_pangkat(2)
print(HASIL)


def display(argument: string):
    print(argument)


display("ucup")
