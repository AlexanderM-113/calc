def p():
    input("Press EXE...")

def limiting_reagent():
    print("\n" + "="*32)
    print("LIMITING REAGENT")
    print("="*32 + "\n")
    
    print("Reactant 1:")
    moles1=float(input("  Moles: "))
    coeff1=float(input("  Coefficient: "))
    
    print("Reactant 2:")
    moles2=float(input("  Moles: "))
    coeff2=float(input("  Coefficient: "))
    
    ratio1=moles1/coeff1
    ratio2=moles2/coeff2
    
    print("\n" + "="*32)
    print("RATIO ANALYSIS")
    print("="*32 + "\n")
    print("Reactant 1 ratio: " + str(round(ratio1,4)))
    print("Reactant 2 ratio: " + str(round(ratio2,4)))
    
    if ratio1<ratio2:
        print("\nLimiting: Reactant 1")
        limit_moles=ratio1
    else:
        print("\nLimiting: Reactant 2")
        limit_moles=ratio2
    
    print("Limiting moles: " + str(round(limit_moles,4)) + "\n")
    p()

def yield_calc():
    print("\n" + "="*32)
    print("YIELD CALCULATION")
    print("="*32 + "\n")
    
    theoretical=float(input("Theoretical yield (g): "))
    actual=float(input("Actual yield (g): "))
    
    percent=(actual/theoretical)*100
    
    print("\n" + "="*32)
    print("PERCENT YIELD")
    print("="*32 + "\n")
    print("% Yield = (actual/theoretical)*100")
    print("% Yield = (" + str(actual) + "/" + str(theoretical) + ")*100")
    print("% Yield = " + str(round(percent,2)) + "%\n")
    p()

while True:
    print("\n" + "="*32)
    print("STOICHIOMETRY")
    print("="*32 + "\n")
    print("1 = Limiting reagent")
    print("2 = Percent yield")
    print("3 = Exit\n")
    ch=input("Choose: ")
    
    if ch=="1":
        limiting_reagent()
    elif ch=="2":
        yield_calc()
    elif ch=="3":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice.")
