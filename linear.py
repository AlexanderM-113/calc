def p():
    input("Press EXE...")

def solve_2x2():
    print("\n" + "="*32)
    print("SOLVE 2x2 SYSTEM")
    print("="*32 + "\n")
    print("Equation 1: a1*x + b1*y = c1")
    print("Equation 2: a2*x + b2*y = c2\n")
    
    a1=float(input("a1: "))
    b1=float(input("b1: "))
    c1=float(input("c1: "))
    
    a2=float(input("a2: "))
    b2=float(input("b2: "))
    c2=float(input("c2: "))
    
    det=a1*b2-a2*b1
    
    print("\n" + "="*32)
    print("DETERMINANT")
    print("="*32 + "\n")
    print("D = a1*b2 - a2*b1")
    print("D = " + str(a1) + "*" + str(b2))
    print("  - " + str(a2) + "*" + str(b1))
    print("D = " + str(round(det,2)) + "\n")
    
    if det==0:
        print("No unique solution (parallel lines)")
        p()
        return
    
    x=(c1*b2-c2*b1)/det
    y=(a1*c2-a2*c1)/det
    
    print("="*32)
    print("SOLUTION")
    print("="*32 + "\n")
    print("x = " + str(round(x,4)))
    print("y = " + str(round(y,4)) + "\n")
    
    print("="*32)
    print("VERIFICATION")
    print("="*32 + "\n")
    eq1=a1*x+b1*y
    eq2=a2*x+b2*y
    print("Eq1: " + str(round(eq1,4)) + " = " + str(c1))
    print("Eq2: " + str(round(eq2,4)) + " = " + str(c2) + "\n")
    p()

def solve_3x3():
    print("\n" + "="*32)
    print("SOLVE 3x3 SYSTEM")
    print("="*32 + "\n")
    print("a1*x + b1*y + c1*z = d1")
    print("a2*x + b2*y + c2*z = d2")
    print("a3*x + b3*y + c3*z = d3\n")
    
    a1=float(input("a1: "))
    b1=float(input("b1: "))
    c1=float(input("c1: "))
    d1=float(input("d1: "))
    
    a2=float(input("a2: "))
    b2=float(input("b2: "))
    c2=float(input("c2: "))
    d2=float(input("d2: "))
    
    a3=float(input("a3: "))
    b3=float(input("b3: "))
    c3=float(input("c3: "))
    d3=float(input("d3: "))
    
    det=(a1*(b2*c3-b3*c2)-b1*(a2*c3-a3*c2)
         +c1*(a2*b3-a3*b2))
    
    print("\n" + "="*32)
    print("DETERMINANT")
    print("="*32 + "\n")
    print("D = " + str(round(det,2)) + "\n")
    
    if det==0:
        print("No unique solution")
        p()
        return
    
    x_det=(d1*(b2*c3-b3*c2)-b1*(d2*c3-d3*c2)
           +c1*(d2*b3-d3*b2))
    y_det=(a1*(d2*c3-d3*c2)-d1*(a2*c3-a3*c2)
           +c1*(a2*d3-a3*d2))
    z_det=(a1*(b2*d3-b3*d2)-b1*(a2*d3-a3*d2)
           +d1*(a2*b3-a3*b2))
    
    x=x_det/det
    y=y_det/det
    z=z_det/det
    
    print("="*32)
    print("SOLUTION")
    print("="*32 + "\n")
    print("x = " + str(round(x,4)))
    print("y = " + str(round(y,4)))
    print("z = " + str(round(z,4)) + "\n")
    p()

while True:
    print("\n" + "="*32)
    print("LINEAR EQUATION SOLVER")
    print("="*32 + "\n")
    print("1 = Solve 2x2 system")
    print("2 = Solve 3x3 system")
    print("3 = Exit\n")
    ch=input("Choose: ")
    
    if ch=="1":
        solve_2x2()
    elif ch=="2":
        solve_3x3()
    elif ch=="3":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice.")
