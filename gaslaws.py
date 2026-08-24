def p():
    input("Press EXE...")

def ideal_gas():
    print("\n" + "="*32)
    print("IDEAL GAS LAW")
    print("="*32 + "\n")
    print("PV = nRT")
    print("R = 0.0821 L*atm/(mol*K)\n")
    
    print("1 = Solve for P")
    print("2 = Solve for V")
    print("3 = Solve for n")
    print("4 = Solve for T\n")
    
    ch=input("Choose: ")
    R=0.0821
    
    if ch=="1":
        n=float(input("n (mol): "))
        v=float(input("V (L): "))
        t=float(input("T (K): "))
        p=n*R*t/v
        print("\nP = nRT/V")
        print("P = " + str(round(p,4)) + " atm\n")
    elif ch=="2":
        n=float(input("n (mol): "))
        p=float(input("P (atm): "))
        t=float(input("T (K): "))
        v=n*R*t/p
        print("\nV = nRT/P")
        print("V = " + str(round(v,4)) + " L\n")
    elif ch=="3":
        p=float(input("P (atm): "))
        v=float(input("V (L): "))
        t=float(input("T (K): "))
        n=p*v/(R*t)
        print("\nn = PV/RT")
        print("n = " + str(round(n,4)) + " mol\n")
    elif ch=="4":
        p=float(input("P (atm): "))
        v=float(input("V (L): "))
        n=float(input("n (mol): "))
        t=p*v/(n*R)
        print("\nT = PV/nR")
        print("T = " + str(round(t,4)) + " K\n")
    
    p()

def combined_gas():
    print("\n" + "="*32)
    print("COMBINED GAS LAW")
    print("="*32 + "\n")
    print("(P1*V1)/T1 = (P2*V2)/T2\n")
    
    print("State 1:")
    p1=float(input("  P (atm): "))
    v1=float(input("  V (L): "))
    t1=float(input("  T (K): "))
    
    print("State 2 (enter 0 for unknown):")
    p2=float(input("  P (atm): "))
    v2=float(input("  V (L): "))
    t2=float(input("  T (K): "))
    
    if p2==0:
        p2=(p1*v1*t2)/(v2*t1)
        print("\nP2 = " + str(round(p2,4)) + " atm\n")
    elif v2==0:
        v2=(p1*v1*t2)/(p2*t1)
        print("\nV2 = " + str(round(v2,4)) + " L\n")
    elif t2==0:
        t2=(p2*v2*t1)/(p1*v1)
        print("\nT2 = " + str(round(t2,4)) + " K\n")
    
    p()

while True:
    print("\n" + "="*32)
    print("GAS LAWS")
    print("="*32 + "\n")
    print("1 = Ideal gas law")
    print("2 = Combined gas law")
    print("3 = Exit\n")
    ch=input("Choose: ")
    
    if ch=="1":
        ideal_gas()
    elif ch=="2":
        combined_gas()
    elif ch=="3":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice.")
