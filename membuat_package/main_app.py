# Cara Membuat Package
import os
import sains.matematika
from sains import fisika
from sains.fisika import gaya as F
os.system("clear")

# Cara memanggil package sama dengan cara memanggil module


print("\n=== cara membuat Package ====")


hasil_tambah = sains.matematika.tambah(1, 2, 3, 4, 5)
print(f"hasil tambah = {hasil_tambah}")

gaya = F(90, 10)
print(f"gaya adalah = {gaya}")
