# Copy And Pop Dictionary

print("\n==== copy & pop dictionary ====")

teman_teman = {
    "cup": "si ucup",
    "tong": "si otong",
    "ding": "si diding ",
    "dung": "si dudung"
}

friends = teman_teman
print(f"teman-teman: {teman_teman}")
print(f"friend : {friends}")

# pop dictionary mengambil berdasarkan (key)
print("=== pop berdasarkan key")
dataAsep = friends.pop("cup")
print(f"teman-teman: {teman_teman}\n")
print(f"friend : {friends}\n")


# popitem mengambil data terakhir
print("=== pop dictionary data terakhir ===")
dataTerakhir = friends.popitem()
print(f"data terkhir = {dataTerakhir}")
print(f"friends = {friends}")
