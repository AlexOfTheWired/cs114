""" Gallon to liter converter """

def LitersPerGallon(gallons):
    gallons = int(input())
    liters_per_gallon = 3.78541

    print("how many gallons?")
    convert_volume = gallons * liters_per_gallon

    print(str(convert_volume) + "liters.")

LitersPerGallon()
