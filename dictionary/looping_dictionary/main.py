# Looping Dictioanry
print("\n===== Looping DIctionary =====\t")
teman_teman = {
    "cup": "ucup si ucup",
    "tong": "otong",
    "dung": "dudung",
    "din": "didin",
    "drn": "drdrn ",

}

keys = teman_teman.keys()

for key in teman_teman.keys():
    print(teman_teman.get(key))


values = teman_teman.values()

for value in teman_teman.values():
    print(value)

items = teman_teman.items()

for item in teman_teman.items():
    print(item)

for key, value in teman_teman.items():
    print(f"key = {key}, value = {value}")
