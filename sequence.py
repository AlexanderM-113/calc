def p():
    input("Press EXE...")

def arithmetic():
    print("\n" + "="*32)
    print("ARITHMETIC SEQUENCE")
    print("="*32 + "\n")
    print("Formula: an = a1 + (n-1)*d\n")
    
    a1=float(input("First term (a1): "))
    d=float(input("Common difference (d): "))
    n=int(input("Number of terms: "))
    
    print("\n" + "="*32)
    print("SEQUENCE")
    print("="*32 + "\n")
    
    for i in range(1,min(n+1,11)):
        an=a1+(i-1)*d
        print(str(i).rjust(2) + ": " + str(round(an,4)))
    
    if n>10:
        print("... (" + str(n-10) + " more terms)")
    
    an=a1+(n-1)*d
    sn=n*(a1+an)/2
    
    print("\n" + "="*32)
    print("NTH TERM & SUM")
    print("="*32 + "\n")
    print("a(" + str(n) + ") = " + str(round(an,4)))
    print("S(" + str(n) + ") = n*(a1+an)/2")
    print("S(" + str(n) + ") = " + str(n) + "*(" + str(round(a1,4))
          + "+" + str(round(an,4)) + ")/2")
    print("S(" + str(n) + ") = " + str(round(sn,4)) + "\n")
    p()

def geometric():
    print("\n" + "="*32)
    print("GEOMETRIC SEQUENCE")
    print("="*32 + "\n")
    print("Formula: an = a1 * r^(n-1)\n")
    
    a1=float(input("First term (a1): "))
    r=float(input("Common ratio (r): "))
    n=int(input("Number of terms: "))
    
    print("\n" + "="*32)
    print("SEQUENCE")
    print("="*32 + "\n")
    
    for i in range(1,min(n+1,11)):
        an=a1*(r**(i-1))
        print(str(i).rjust(2) + ": " + str(round(an,4)))
    
    if n>10:
        print("... (" + str(n-10) + " more terms)")
    
    an=a1*(r**(n-1))
    
    if abs(r)==1:
        sn=a1*n
    else:
        sn=a1*(1-r**n)/(1-r)
    
    print("\n" + "="*32)
    print("NTH TERM & SUM")
    print("="*32 + "\n")
    print("a(" + str(n) + ") = " + str(round(an,4)))
    print("S(" + str(n) + ") = a1*(1-r^n)/(1-r)")
    print("S(" + str(n) + ") = " + str(round(sn,4)) + "\n")
    
    if abs(r)<1:
        s_inf=a1/(1-r)
        print("Infinite sum = " + str(round(s_inf,4)) + "\n")
    
    p()

while True:
    print("\n" + "="*32)
    print("SEQUENCE/SERIES HELPER")
    print("="*32 + "\n")
    print("1 = Arithmetic sequence")
    print("2 = Geometric sequence")
    print("3 = Exit\n")
    ch=input("Choose: ")
    
    if ch=="1":
        arithmetic()
    elif ch=="2":
        geometric()
    elif ch=="3":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice.")
