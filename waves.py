import math

def p():
    input("Press EXE...")

def frequency_wavelength():
    print("\n" + "="*32)
    print("FREQUENCY & WAVELENGTH")
    print("="*32 + "\n")
    print("Formula: v = f * lambda\n")
    
    print("1 = Find wavelength")
    print("2 = Find frequency")
    ch=input("Choose: ")
    
    if ch=="1":
        f=float(input("Frequency (Hz): "))
        v=float(input("Speed (m/s): "))
        wave=v/f
        print("\nlambda = " + str(v) + "/" + str(f))
        print("lambda = " + str(round(wave,4)) + " m\n")
    elif ch=="2":
        wave=float(input("Wavelength (m): "))
        v=float(input("Speed (m/s): "))
        f=v/wave
        print("\nf = " + str(v) + "/" + str(wave))
        print("f = " + str(round(f,4)) + " Hz\n")
    
    p()

def doppler():
    print("\n" + "="*32)
    print("DOPPLER EFFECT")
    print("="*32 + "\n")
    print("f' = f*(v+vo)/(v-vs)\n")
    
    f=float(input("Frequency (Hz): "))
    v=float(input("Sound speed (m/s): "))
    vs=float(input("Source velocity (m/s): "))
    vo=float(input("Observer velocity (m/s): "))
    
    if v==vs:
        print("\nError: source at sound speed")
        p()
        return
    
    f_prime=f*(v+vo)/(v-vs)
    
    print("\nf' = " + str(f) + "*(" + str(v) + "+" + str(vo))
    print("    /(" + str(v) + "-" + str(vs) + "))")
    print("f' = " + str(round(f_prime,2)) + " Hz\n")
    p()

def decibels():
    print("\n" + "="*32)
    print("DECIBELS")
    print("="*32 + "\n")
    print("dB = 10*log10(I/I0)\n")
    
    i=float(input("Intensity (W/m2): "))
    i0=1e-12
    
    db=10*math.log10(i/i0)
    
    print("\nI0 = 1e-12 W/m2 (reference)")
    print("dB = 10*log10(" + str(i) + "/1e-12)")
    print("dB = " + str(round(db,2)) + "\n")
    p()

while True:
    print("\n" + "="*32)
    print("WAVES & SOUND")
    print("="*32 + "\n")
    print("1 = Frequency/Wavelength")
    print("2 = Doppler effect")
    print("3 = Decibels")
    print("4 = Exit\n")
    ch=input("Choose: ")
    
    if ch=="1":
        frequency_wavelength()
    elif ch=="2":
        doppler()
    elif ch=="3":
        decibels()
    elif ch=="4":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice.")
