def p():
    input("Press EXE...")

def temperature():
    print("\n" + "="*32)
    print("TEMPERATURE CONVERTER")
    print("="*32 + "\n")
    print("1 = Celsius to Fahrenheit")
    print("2 = Fahrenheit to Celsius")
    print("3 = Celsius to Kelvin")
    print("4 = Kelvin to Celsius\n")
    
    ch=input("Choose: ")
    val=float(input("Value: "))
    
    if ch=="1":
        result=val*9/5+32
        print("\n" + str(val) + "C = " + str(round(result,2)) + "F\n")
    elif ch=="2":
        result=(val-32)*5/9
        print("\n" + str(val) + "F = " + str(round(result,2)) + "C\n")
    elif ch=="3":
        result=val+273.15
        print("\n" + str(val) + "C = " + str(round(result,2)) + "K\n")
    elif ch=="4":
        result=val-273.15
        print("\n" + str(val) + "K = " + str(round(result,2)) + "C\n")
    else:
        print("\nInvalid")
    
    p()

def distance():
    print("\n" + "="*32)
    print("DISTANCE CONVERTER")
    print("="*32 + "\n")
    print("1 = Meters to Feet")
    print("2 = Feet to Meters")
    print("3 = Miles to Kilometers")
    print("4 = Kilometers to Miles")
    print("5 = Inches to Centimeters\n")
    
    ch=input("Choose: ")
    val=float(input("Value: "))
    
    if ch=="1":
        result=val*3.28084
        print("\n" + str(val) + "m = " + str(round(result,2)) + "ft\n")
    elif ch=="2":
        result=val/3.28084
        print("\n" + str(val) + "ft = " + str(round(result,2)) + "m\n")
    elif ch=="3":
        result=val*1.60934
        print("\n" + str(val) + "mi = " + str(round(result,2)) + "km\n")
    elif ch=="4":
        result=val/1.60934
        print("\n" + str(val) + "km = " + str(round(result,2)) + "mi\n")
    elif ch=="5":
        result=val*2.54
        print("\n" + str(val) + "in = " + str(round(result,2)) + "cm\n")
    else:
        print("\nInvalid")
    
    p()

def weight():
    print("\n" + "="*32)
    print("WEIGHT CONVERTER")
    print("="*32 + "\n")
    print("1 = Kilograms to Pounds")
    print("2 = Pounds to Kilograms")
    print("3 = Grams to Ounces")
    print("4 = Ounces to Grams\n")
    
    ch=input("Choose: ")
    val=float(input("Value: "))
    
    if ch=="1":
        result=val*2.20462
        print("\n" + str(val) + "kg = " + str(round(result,2)) + "lb\n")
    elif ch=="2":
        result=val/2.20462
        print("\n" + str(val) + "lb = " + str(round(result,2)) + "kg\n")
    elif ch=="3":
        result=val/28.3495
        print("\n" + str(val) + "g = " + str(round(result,2)) + "oz\n")
    elif ch=="4":
        result=val*28.3495
        print("\n" + str(val) + "oz = " + str(round(result,2)) + "g\n")
    else:
        print("\nInvalid")
    
    p()

def volume():
    print("\n" + "="*32)
    print("VOLUME CONVERTER")
    print("="*32 + "\n")
    print("1 = Liters to Gallons")
    print("2 = Gallons to Liters")
    print("3 = Milliliters to Cups")
    print("4 = Cups to Milliliters\n")
    
    ch=input("Choose: ")
    val=float(input("Value: "))
    
    if ch=="1":
        result=val*0.264172
        print("\n" + str(val) + "L = " + str(round(result,2)) + "gal\n")
    elif ch=="2":
        result=val/0.264172
        print("\n" + str(val) + "gal = " + str(round(result,2)) + "L\n")
    elif ch=="3":
        result=val/236.588
        print("\n" + str(val) + "mL = " + str(round(result,2)) + "cup\n")
    elif ch=="4":
        result=val*236.588
        print("\n" + str(val) + "cup = " + str(round(result,2)) + "mL\n")
    else:
        print("\nInvalid")
    
    p()

def speed():
    print("\n" + "="*32)
    print("SPEED CONVERTER")
    print("="*32 + "\n")
    print("1 = m/s to km/h")
    print("2 = km/h to m/s")
    print("3 = m/s to mph")
    print("4 = mph to m/s\n")
    
    ch=input("Choose: ")
    val=float(input("Value: "))
    
    if ch=="1":
        result=val*3.6
        print("\n" + str(val) + "m/s = " + str(round(result,2)) + "km/h\n")
    elif ch=="2":
        result=val/3.6
        print("\n" + str(val) + "km/h = " + str(round(result,2)) + "m/s\n")
    elif ch=="3":
        result=val*2.23694
        print("\n" + str(val) + "m/s = " + str(round(result,2)) + "mph\n")
    elif ch=="4":
        result=val/2.23694
        print("\n" + str(val) + "mph = " + str(round(result,2)) + "m/s\n")
    else:
        print("\nInvalid")
    
    p()

while True:
    print("\n" + "="*32)
    print("UNIT CONVERTER")
    print("="*32 + "\n")
    print("1 = Temperature")
    print("2 = Distance")
    print("3 = Weight")
    print("4 = Volume")
    print("5 = Speed")
    print("6 = Exit\n")
    ch=input("Choose: ")
    
    if ch=="1":
        temperature()
    elif ch=="2":
        distance()
    elif ch=="3":
        weight()
    elif ch=="4":
        volume()
    elif ch=="5":
        speed()
    elif ch=="6":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice.")
