# String width alignment


# width and multiline

# Data

data_nama = "ucup"
data_umur = 17
data_tinggi = 170.1
data_nomor_sepatu = 41


# String
data_string = f"nama = {data_nama} , umur = {data_umur} , tinggi = {data_tinggi} , sepatu = {data_nomor_sepatu}"
print("\n"+5*"=" + "Data String" + 5*"=")
print(data_string)

# String multiline (dengan menggunakan enter / new line \n)
data_string = f" nama = {data_nama} \n umur = {data_umur}  \n tinggi = {data_tinggi}  \n sepatu = {data_nomor_sepatu}"
print("\n"+5*"=" + "String multiline (enter)" + 5*"=")
print(data_string)

# String multiline dengan (kutip triplet)

data_string = f"""nama   = {data_nama}
umur   = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print("\n"+5*"=" + "String multiline (kutip triplet)" + 5*"=")
print(data_string)

# mengatur lebar

data_string = f"""nama   = {data_nama:>5}
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomor_sepatu:>5}
"""
print("\n"+5*"=" + "String multiline (kutip triplet)" + 5*"=")
print(data_string)
