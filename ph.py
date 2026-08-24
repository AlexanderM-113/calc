import math

def p():
    input("Press EXE...")

def ph_from_h():
    print("\n" + "="*32)
    print("pH FROM [H+]")
    print("="*32 + "\n")
    print("pH = -log10[H+]\n")
    
    h=float(input("[H+] concentration: "))
    ph=-math.log10(h)
    poh=14-ph
    
    print("\npH = -log10(" + str(h) + ")")
    print("pH = " + str(round(ph,2)))
    print("pOH = " + str(round(poh,2)) + "\n")
    p()

def h_from_ph():
    print("\n" + "="*32)
    print("[H+] FROM pH")
    print("="*32 + "\n")
    print("[H+] = 10^(-pH)\n")
    
    ph=float(input("pH: "))
    h=10**(-ph)
    
    print("\n[H+] = 10^(-" + str(ph) + ")")
    print("[H+] = " + str(h) + " M\n")
    p()

def poh_from_oh():
    print("\n" + "="*32)
    print("pOH FROM [OH-]")
    print("="*32 + "\n")
    print("pOH = -log10[OH-]\n")
    
    oh=float(input("[OH-] concentration: "))
    poh=-math.log10(oh)
    ph=14-poh
    
    print("\npOH = -log10(" + str(oh) + ")")
    print("pOH = " + str(round(poh,2)))
    print("pH = " + str(round(ph,2)) + "\n")
    p()

while True:
    print("\n" + "="*32)
    print("pH CALCULATOR")
    print("="*32 + "\n")
    print("1 = pH from [H+]")
    print("2 = [H+] from pH")
    print("3 = pOH from [OH-]")
    print("4 = Exit\n")
    ch=input("Choose: ")
    
    if ch=="1":
        ph_from_h()
    elif ch=="2":
        h_from_ph()
    elif ch=="3":
        poh_from_oh()
    elif ch=="4":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice.")
