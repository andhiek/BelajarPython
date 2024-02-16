from matematika import pangkat as p
from matematika import kali as l
from matematika import tambah as add

import matematika as math
print("\n===== cara menggunakan Alias ====")

# from matematika import *


hasil_tambah = add(1, 2, 3, 4, 5)

print(f"hasil tambah = {hasil_tambah}")

hasil_kali = math.l(1, 2, 3, 4, 5)
print(f"hasil kali = {hasil_kali}")

pangkat_3 = p(3)
print(f"ini hasil pangkat 3 = {pangkat_3(3) }")
