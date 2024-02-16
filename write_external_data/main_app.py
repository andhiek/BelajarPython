# write external data


print(3*"=", "menulis file external dengan open", 3*"=")

with open("data_1.txt", 'w', encoding="utf-8") as file:
    file.write("ucup surucup")

with open("data_1.txt", 'w', encoding="utf-8") as file:
    file.write("ini akan meng overwrite isi data")

# cara di atas akan menimpa isi file


# 2 . mode append (data akan bertambah)

with open("data_2.txt", 'a', encoding="utf-8") as file:
    file.write("joni si joni\n")

with open("data_2.txt", 'w', encoding="utf-8") as file:
    file.write("ucup surucup\n")

with open("data_2.txt", 'a', encoding="utf-8") as file:
    file.write("joni si joni\n")

with open("data_2.txt", 'a', encoding="utf-8") as file:
    file.write("data akan bertambah dengan mode append")


# 3 . mode r+

with open("data_3.txt", 'w', encoding="utf-8") as file:
    file.write("ini adalah data ke 3\n")


with open("data_3.txt", 'r+', encoding="utf-8") as file:
    file.write("menambah data dengan r+\n")
    file.write("baris ke-1\n")
    file.write("baris ke-2\n")
    file.write("baris ke-3\n")


with open("data_3.txt", 'r+', encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("data_3.txt", 'r+', encoding="utf-8") as file:
    file.write("otong surotong\n")

with open("data_3.txt", 'r+', encoding="utf-8") as file:
    # akan menimpa isi text data sesuai dengan panjang data
    file.write("mode r+ akan menimpa isi data")
