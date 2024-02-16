# Operasi Dictionary
print("\n===== Operasi Dictionary ======\n")

data_dict = {
    'cup': 'ucup surucup',
    'tong': 'otong surotong',
    'dung': 'dudung surudung',
}

# mengambil panjang dictionary
print("*mengambil panjang dictionary*")
LENDICT = len(data_dict)
print(f" panjang dari data_dict = {LENDICT}")

# mengecek key exist atau tidak
print("\n*mengecek key exist / tidak*")
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict = {CHECKKEY}")

# mengakses value
print("\n*mengakses value*")
print(data_dict.get("cup", "key tidak ditemukan"))
print(data_dict.get("kis"))
# cek key dengan message tidak ditemukan
print(data_dict.get("kis", "key tidak ditemukan"))

# mengupdate data dictionary
data_dict["cup"] = " ucup si ganteng"
print(data_dict)
data_dict["sep"] = "asep si kasyep"
print(data_dict)
data_dict.update({"cup": "ucup surucup"})
print(data_dict)
data_dict.update({"dan": "danny si ganteng"})
print(data_dict)
