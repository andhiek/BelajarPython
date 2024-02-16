# Menggunakan standart libary yang ada di python

import io
from collections import Counter
import datetime


data_waktu = datetime.datetime.now()

print(f"datetime.now: {data_waktu}")
print(f"tahun : {data_waktu.year}")
print(f"tahun : {data_waktu.strftime('%A')}")


data = ["a", "b", "c", "d", "e", "a", "a", "b", "c"]

data_count = Counter(data)

print(f"ini  adalah data count = {data_count}")
print(f"jumlah data a : {data_count['a']}")
print(f"jumlah data a : {data_count['b']}")


file = io.open("file_text.txt", "r")
