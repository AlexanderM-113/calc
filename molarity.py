def p():
    input("Press EXE...")

def molarity():
    print("\n" + "="*32)
    print("MOLARITY CALCULATION")
    print("="*32 + "\n")
    print("M = moles/volume(L)\n")
    
    print("1 = Find M")
    print("2 = Find moles")
    print("3 = Find volume\n")
    
    ch=input("Choose: ")
    
    if ch=="1":
        moles=float(input("Moles: "))
        vol=float(input("Volume (L): "))
        m=moles/vol
        print("\nM = " + str(moles) + "/" + str(vol))
        print("M = " + str(round(m,4)) + " mol/L\n")
    elif ch=="2":
        m=float(input("Molarity (M): "))
        vol=float(input("Volume (L): "))
        moles=m*vol
        print("\nmoles = M*V")
        print("moles = " + str(round(moles,4)) + "\n")
    elif ch=="3":
        m=float(input("Molarity (M): "))
        moles=float(input("Moles: "))
        vol=moles/m
        print("\nV = moles/M")
        print("V = " + str(round(vol,4)) + " L\n")
    
    p()

def dilution():
    print("\n" + "="*32)
    print("DILUTION (M1V1 = M2V2)")
    print("="*32 + "\n")
    
    print("Initial solution:")
    m1=float(input("  M1: "))
    v1=float(input("  V1 (mL): "))
    
    print("Final solution (enter 0 for unknown):")
    m2=float(input("  M2: "))
    v2=float(input("  V2 (mL): "))
    
    if m2==0:
        m2=(m1*v1)/v2
        print("\nM2 = " + str(round(m2,4)) + " M\n")
    elif v2==0:
        v2=(m1*v1)/m2
        print("\nV2 = " + str(round(v2,4)) + " mL\n")
    
    p()

while True:
    print("\n" + "="*32)
    print("MOLARITY/DILUTION")
    print("="*32 + "\n")
    print("1 = Molarity calculations")
    print("2 = Dilution M1V1=M2V2")
    print("3 = Exit\n")
    ch=input("Choose: ")
    
    if ch=="1":
        molarity()
    elif ch=="2":
        dilution()
    elif ch=="3":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice.")
