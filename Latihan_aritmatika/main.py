# Latihan Satuan konversi Temperatur

print("\nPROGRAM KONVERSI TEMPERATURE\n")
celcius = float(input("Masukan suhu dalam celcius :"))
print("suhu adalah =", celcius, "Celcius")


# Reamur
reamur = (4/5)*celcius
print("suhu dalam reamur =", reamur, "reamur")

# Fahrenheit

fahrenheit = ((9/5)*celcius) + 32
print("suhu dalam fahrenheit =", fahrenheit, "fahrenheit")

# Kelvin
kelvin = celcius + 273
print("suhu dalam kelvin =", kelvin, "kelvin")

print("\nKonversi Fahreinheit ke kelvin \n")
fahrenheit = float(input("Masukan suhu dalam Fahrenheit ="))
print(fahrenheit, "fahrenheit")

# kelvin
kelvin = (fahrenheit - 32) * 5/9 + 273.15
print(kelvin, "kelvin")

print("\nKonversi kelvin ke fahrenheit \n")

kelvin = float(input("Masukan suhu dalam kelvin ="))

fahrenheit = (kelvin - 273.15) * 9/5 + 32
print(fahrenheit, "fahrenheit")
