import math

def p():
    input("Press EXE...")

def solve():
    print("\n" + "="*32)
    print("QUADRATIC FORMULA SOLVER")
    print("="*32 + "\n")
    print("Equation: ax^2 + bx + c = 0\n")
    
    a=float(input("a: "))
    b=float(input("b: "))
    c=float(input("c: "))
    
    if a==0:
        print("\nNot quadratic (a cannot be 0)")
        p()
        return
    
    print("\n" + "="*32)
    print("STEP 1: DISCRIMINANT")
    print("="*32 + "\n")
    print("Formula: D = b^2 - 4ac")
    print("D = " + str(b) + "^2 - 4*" + str(a))
    print("   *" + str(c))
    
    d=b*b-4*a*c
    print("D = " + str(round(d,2)) + "\n")
    
    if d>0:
        print("D > 0: TWO REAL ROOTS\n")
    elif d==0:
        print("D = 0: ONE ROOT\n")
    else:
        print("D < 0: NO REAL ROOTS\n")
    
    p()
    
    print("\n" + "="*32)
    print("STEP 2: QUADRATIC FORMULA")
    print("="*32 + "\n")
    print("x = (-b +/- sqrt(D)) / (2a)\n")
    
    if d<0:
        print("No real solutions")
        p()
        return
    
    sqrt_d=math.sqrt(d)
    x1=(-b+sqrt_d)/(2*a)
    x2=(-b-sqrt_d)/(2*a)
    
    print("x = (-" + str(b) + " +/- sqrt(" + str(d) + "))")
    print("    / (2*" + str(a) + ")")
    print("x = (-" + str(b) + " +/- " + str(round(sqrt_d,2)))
    print("    / " + str(2*a) + "\n")
    
    print("x1 = " + str(round(x1,4)))
    print("x2 = " + str(round(x2,4)) + "\n")
    p()
    
    print("\n" + "="*32)
    print("VERIFICATION")
    print("="*32 + "\n")
    y1=a*x1*x1+b*x1+c
    y2=a*x2*x2+b*x2+c
    print("f(x1) = " + str(round(y1,6)))
    print("f(x2) = " + str(round(y2,6)) + "\n")
    p()

while True:
    print("\n" + "="*32)
    print("QUADRATIC SOLVER")
    print("="*32 + "\n")
    print("1 = Solve equation")
    print("2 = Exit\n")
    ch=input("Choose: ")
    
    if ch=="1":
        solve()
    elif ch=="2":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice.")
