def p():
    input("Press EXE...")

atoms={
    "H":1.008,"C":12.011,"N":14.007,"O":15.999,
    "S":32.065,"P":30.974,"Cl":35.453,"Br":79.904,
    "I":126.904,"Na":22.990,"K":39.098,"Ca":40.078,
    "Mg":24.305,"Al":26.982,"Fe":55.845,"Cu":63.546,
    "Zn":65.38,"F":18.998,"B":10.811
}

def calculate():
    print("\n" + "="*32)
    print("MOLAR MASS CALCULATOR")
    print("="*32 + "\n")
    print("Atoms available:")
    print("H,C,N,O,S,P,Cl,Br,I")
    print("Na,K,Ca,Mg,Al,Fe,Cu,Zn,F,B\n")
    
    print("Enter formula (no spaces)")
    print("Example: H2O, C6H12O6, NaCl\n")
    
    formula=input("Formula: ")
    
    mass=0
    i=0
    while i<len(formula):
        if formula[i].isupper():
            elem=formula[i]
            i+=1
            if i<len(formula) and formula[i].islower():
                elem+=formula[i]
                i+=1
            
            count_str=""
            while i<len(formula) and formula[i].isdigit():
                count_str+=formula[i]
                i+=1
            
            count=int(count_str) if count_str else 1
            
            if elem in atoms:
                mass+=atoms[elem]*count
                print(elem + str(count) + ": " + 
                      str(round(atoms[elem]*count,3)))
            else:
                print("Element " + elem + " not found")
        else:
            i+=1
    
    print("\n" + "="*32)
    print("MOLAR MASS")
    print("="*32 + "\n")
    print(formula + " = " + str(round(mass,3)) + " g/mol\n")
    p()

while True:
    print("\n" + "="*32)
    print("MOLAR MASS")
    print("="*32 + "\n")
    print("1 = Calculate")
    print("2 = Exit\n")
    ch=input("Choose: ")
    
    if ch=="1":
        calculate()
    elif ch=="2":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice.")
