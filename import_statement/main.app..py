# Import Statement

# fungsinya untuk mengambil libary / program dari luar
# Program dari file dari external .py


# 1 Menyambung program dari external
import mathematika
import program_ucup
import program_print
import variable
import kucuy
print("\n ===== import statement ====")


# 2. import dengan data
# data ada di namespace variable

print(variable.data)
print(kucuy.data)

# import dengan fungsi

hasil = mathematika.tambah(4, 5)
print(hasil)
