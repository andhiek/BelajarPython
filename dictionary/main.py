# List -> array ,mengakses dengan menggunakan index
print("\n===== LIST =====\n")

data_list = ["ucup", "otong", "dudung"]
print(data_list)
print(f"index ke 0 dari  data_list : {data_list[0]}")
print(f"index ke 1 dari  data_list : {data_list[1]}")
print(f"index ke 2 dari  data_list : {data_list[2]}")

# Dictionary (dict) -> associative array
# untuk mengakses datanya dengan identifier -> key
print("\n===== DICTIONARY =====\n")

data_dict = {
    'key1': 'ucup',
    'key2': 'otong',
    'dg': 'dudung',
    'number': 1000,
    'list': data_list
}
print(data_dict)
print(f"key1 dari data_dict =  {data_dict['key1']}")
print(f"key2 dari data_dict =  {data_dict['key2']}")
print(f"key3 dari data_dict =  {data_dict['dg']}")
print(f"key4 dari data_dict =  {data_dict['number']}")
print(f"key5 dari data_dict =  {data_dict['list']}")
