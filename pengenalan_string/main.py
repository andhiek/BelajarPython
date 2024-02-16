# Pengenalan String


data = "ini adalah string"
print('data = ', data)
print('data = ', type(data))

# 1. cara membuat String

'''
  1. dengan menggunakan single quote ',,,,,'
  2. dengan menggunakan double quote ",,,,,"
'''

data = "' Menggunakan single quote'"
print(data)
data = '" Menggunakan double quote"'
print(data)
print('"menggabungkan dua quote"')
print("ini adalah hari jum'at")


# 2.Menggunakan tanda \
# membuat tanda ' menjadi string
print('ini adalah hari jum\'at')
print('g\'day,isn\'t it?')

# backslash menjadi string
print("C:\\user\\Ucup")
# tab
print("ucup otong")
print("ucup\t otong")

# membuat backspace
print("ucup otong")
print("ucup \botong")

# newLine
print("baris pertama . \nbaris kedua.")  # LF -> line Feed ->Digunakan di Unic
# CR -> Carriage return -> Commodore , acorn , Lisp
print("baris pertama. \rbaris kedua.")
# CRLF -> Line feed Carriage Return -> Windows
print("baris pertama. \r\nbaris kedua.")


# 3. String Literal atau Raw

# hati- hati
print('C:\\new Folder')

# Menggunakan Raw string
print(r'C:\new Folder')

# MultiLine Literal string
print("""
Nama : Ucup
Kelas :3 SD
""")

# Multiline Literal string dan raw
print(r"""
Nama : Ucup
Kelas :3 SD
website : www.ucup.com/newID
""")
