def p():
    input("Press EXE...")

def solve_2x2_subst():
    print("\n" + "="*32)
    print("2x2 SYSTEM - SUBSTITUTION")
    print("="*32 + "\n")
    print("Equation 1: a1*x + b1*y = c1")
    print("Equation 2: a2*x + b2*y = c2\n")
    
    a1=float(input("Eq1 - a1: "))
    b1=float(input("Eq1 - b1: "))
    c1=float(input("Eq1 - c1: "))
    
    a2=float(input("Eq2 - a2: "))
    b2=float(input("Eq2 - b2: "))
    c2=float(input("Eq2 - c2: "))
    
    print("\n" + "="*32)
    print("STEP 1: SOLVE EQ1 FOR X")
    print("="*32 + "\n")
    print(str(a1) + "*x + " + str(b1) + "*y = " + str(c1))
    print(str(a1) + "*x = " + str(c1) + " - " + str(b1) + "*y")
    
    if a1==0:
        print("\nError: a1 cannot be 0")
        p()
        return
    
    print("x = (" + str(c1) + " - " + str(b1) + "*y)/" + str(a1))
    print()
    p()
    
    print("\n" + "="*32)
    print("STEP 2: SUBSTITUTE INTO EQ2")
    print("="*32 + "\n")
    print(str(a2) + "*(" + str(c1) + " - " + str(b1)
          + "*y)/" + str(a1) + " + " + str(b2) + "*y = " + str(c2))
    
    coeff_y=(a2*b1/a1)+b2
    const=(a2*c1/a1)-c2
    
    if coeff_y==0:
        print("\nNo unique solution (parallel lines)")
        p()
        return
    
    print("\n" + "="*32)
    print("STEP 3: SOLVE FOR Y")
    print("="*32 + "\n")
    print("Simplified: " + str(round(coeff_y,4)) + "*y = " 
          + str(round(const,4)))
    
    y=const/coeff_y
    print("y = " + str(round(y,4)) + "\n")
    p()
    
    print("\n" + "="*32)
    print("STEP 4: SUBSTITUTE BACK")
    print("="*32 + "\n")
    print("x = (" + str(c1) + " - " + str(b1) + "*" + str(round(y,4))
          + ")/" + str(a1))
    
    x=(c1-b1*y)/a1
    print("x = " + str(round(x,4)) + "\n")
    p()
    
    print("\n" + "="*32)
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

def solve_2x2_elim():
    print("\n" + "="*32)
    print("2x2 SYSTEM - ELIMINATION")
    print("="*32 + "\n")
    print("Equation 1: a1*x + b1*y = c1")
    print("Equation 2: a2*x + b2*y = c2\n")
    
    a1=float(input("Eq1 - a1: "))
    b1=float(input("Eq1 - b1: "))
    c1=float(input("Eq1 - c1: "))
    
    a2=float(input("Eq2 - a2: "))
    b2=float(input("Eq2 - b2: "))
    c2=float(input("Eq2 - c2: "))
    
    print("\n" + "="*32)
    print("STEP 1: ELIMINATE X")
    print("="*32 + "\n")
    print("Eq1: " + str(a1) + "*x + " + str(b1) + "*y = " + str(c1))
    print("Eq2: " + str(a2) + "*x + " + str(b2) + "*y = " + str(c2))
    
    m1=a2
    m2=a1
    
    print("\nMultiply Eq1 by " + str(m1))
    print("Multiply Eq2 by -" + str(m2))
    
    new_a1=a1*m1
    new_b1=b1*m1
    new_c1=c1*m1
    
    new_a2=a2*(-m2)
    new_b2=b2*(-m2)
    new_c2=c2*(-m2)
    
    print("\nEq1*" + str(m1) + ": " + str(round(new_a1,4)) + "*x + " 
          + str(round(new_b1,4)) + "*y = " + str(round(new_c1,4)))
    print("Eq2*-" + str(m2) + ": " + str(round(new_a2,4)) + "*x + "
          + str(round(new_b2,4)) + "*y = " + str(round(new_c2,4)))
    
    p()
    
    print("\n" + "="*32)
    print("STEP 2: ADD EQUATIONS")
    print("="*32 + "\n")
    
    coeff_y=new_b1+new_b2
    const=new_c1+new_c2
    
    print("Adding: " + str(round(coeff_y,4)) + "*y = " 
          + str(round(const,4)))
    
    if coeff_y==0:
        print("\nNo unique solution")
        p()
        return
    
    y=const/coeff_y
    print("\ny = " + str(round(y,4)) + "\n")
    p()
    
    print("\n" + "="*32)
    print("STEP 3: SUBSTITUTE BACK")
    print("="*32 + "\n")
    print(str(a1) + "*x + " + str(b1) + "*" + str(round(y,4))
          + " = " + str(c1))
    
    x=(c1-b1*y)/a1
    print("x = " + str(round(x,4)) + "\n")
    p()
    
    print("\n" + "="*32)
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

def solve_3x3_subst():
    print("\n" + "="*32)
    print("3x3 SYSTEM - SUBSTITUTION")
    print("="*32 + "\n")
    print("a1*x + b1*y + c1*z = d1")
    print("a2*x + b2*y + c2*z = d2")
    print("a3*x + b3*y + c3*z = d3\n")
    
    a1=float(input("Eq1 - a1: "))
    b1=float(input("Eq1 - b1: "))
    c1=float(input("Eq1 - c1: "))
    d1=float(input("Eq1 - d1: "))
    
    a2=float(input("Eq2 - a2: "))
    b2=float(input("Eq2 - b2: "))
    c2=float(input("Eq2 - c2: "))
    d2=float(input("Eq2 - d2: "))
    
    a3=float(input("Eq3 - a3: "))
    b3=float(input("Eq3 - b3: "))
    c3=float(input("Eq3 - c3: "))
    d3=float(input("Eq3 - d3: "))
    
    print("\n" + "="*32)
    print("STEP 1: SOLVE EQ1 FOR X")
    print("="*32 + "\n")
    print(str(a1) + "*x + " + str(b1) + "*y + " + str(c1) 
          + "*z = " + str(d1))
    print(str(a1) + "*x = " + str(d1) + " - " + str(b1) + "*y - "
          + str(c1) + "*z")
    
    if a1==0:
        print("\nError: a1 cannot be 0")
        p()
        return
    
    print("x = (" + str(d1) + " - " + str(b1) + "*y - " + str(c1)
          + "*z)/" + str(a1) + "\n")
    p()
    
    print("\n" + "="*32)
    print("STEP 2: SUBSTITUTE INTO EQ2 & EQ3")
    print("="*32 + "\n")
    
    m_b=(a2*b1/a1)-b2
    m_c=(a2*c1/a1)-c2
    m_d=(a2*d1/a1)-d2
    
    n_b=(a3*b1/a1)-b3
    n_c=(a3*c1/a1)-c3
    n_d=(a3*d1/a1)-d3
    
    print("New Eq2: " + str(round(m_b,4)) + "*y + " 
          + str(round(m_c,4)) + "*z = " + str(round(m_d,4)))
    print("New Eq3: " + str(round(n_b,4)) + "*y + " 
          + str(round(n_c,4)) + "*z = " + str(round(n_d,4)) + "\n")
    p()
    
    print("\n" + "="*32)
    print("STEP 3: SOLVE 2x2 SUBSYSTEM")
    print("="*32 + "\n")
    
    if m_b==0:
        print("Error: cannot solve")
        p()
        return
    
    print("Solving for y and z...\n")
    p()
    
    z_coeff=(n_b*m_c/m_b)-n_c
    z_const=(n_b*m_d/m_b)-n_d
    
    if z_coeff==0:
        print("No unique solution")
        p()
        return
    
    z=z_const/z_coeff
    y=(m_d-m_c*z)/m_b
    x=(d1-b1*y-c1*z)/a1
    
    print("\n" + "="*32)
    print("STEP 4: BACK SUBSTITUTION")
    print("="*32 + "\n")
    print("z = " + str(round(z,4)))
    print("y = " + str(round(y,4)))
    print("x = " + str(round(x,4)) + "\n")
    p()
    
    print("\n" + "="*32)
    print("SOLUTION")
    print("="*32 + "\n")
    print("x = " + str(round(x,4)))
    print("y = " + str(round(y,4)))
    print("z = " + str(round(z,4)) + "\n")
    
    print("="*32)
    print("VERIFICATION")
    print("="*32 + "\n")
    eq1=a1*x+b1*y+c1*z
    eq2=a2*x+b2*y+c2*z
    eq3=a3*x+b3*y+c3*z
    print("Eq1: " + str(round(eq1,4)) + " = " + str(d1))
    print("Eq2: " + str(round(eq2,4)) + " = " + str(d2))
    print("Eq3: " + str(round(eq3,4)) + " = " + str(d3) + "\n")
    p()

def solve_3x3_elim():
    print("\n" + "="*32)
    print("3x3 SYSTEM - ELIMINATION")
    print("="*32 + "\n")
    print("a1*x + b1*y + c1*z = d1")
    print("a2*x + b2*y + c2*z = d2")
    print("a3*x + b3*y + c3*z = d3\n")
    
    a1=float(input("Eq1 - a1: "))
    b1=float(input("Eq1 - b1: "))
    c1=float(input("Eq1 - c1: "))
    d1=float(input("Eq1 - d1: "))
    
    a2=float(input("Eq2 - a2: "))
    b2=float(input("Eq2 - b2: "))
    c2=float(input("Eq2 - c2: "))
    d2=float(input("Eq2 - d2: "))
    
    a3=float(input("Eq3 - a3: "))
    b3=float(input("Eq3 - b3: "))
    c3=float(input("Eq3 - c3: "))
    d3=float(input("Eq3 - d3: "))
    
    print("\n" + "="*32)
    print("STEP 1: ELIMINATE X FROM EQ2")
    print("="*32 + "\n")
    print("Eq1: " + str(a1) + "*x + " + str(b1) + "*y + " + str(c1)
          + "*z = " + str(d1))
    print("Eq2: " + str(a2) + "*x + " + str(b2) + "*y + " + str(c2)
          + "*z = " + str(d2))
    
    m1=a2
    m2=a1
    
    new_a2=a2*m1-a1*m2
    new_b2=b2*m1-b1*m2
    new_c2=c2*m1-c1*m2
    new_d2=d2*m1-d1*m2
    
    print("\nEq2*" + str(m1) + " - Eq1*" + str(m2) + ":")
    print(str(round(new_b2,4)) + "*y + " + str(round(new_c2,4))
          + "*z = " + str(round(new_d2,4)) + "\n")
    p()
    
    print("\n" + "="*32)
    print("STEP 2: ELIMINATE X FROM EQ3")
    print("="*32 + "\n")
    print("Eq1: " + str(a1) + "*x + " + str(b1) + "*y + " + str(c1)
          + "*z = " + str(d1))
    print("Eq3: " + str(a3) + "*x + " + str(b3) + "*y + " + str(c3)
          + "*z = " + str(d3))
    
    m3=a3
    m4=a1
    
    new_a3=a3*m3-a1*m4
    new_b3=b3*m3-b1*m4
    new_c3=c3*m3-c1*m4
    new_d3=d3*m3-d1*m4
    
    print("\nEq3*" + str(m3) + " - Eq1*" + str(m4) + ":")
    print(str(round(new_b3,4)) + "*y + " + str(round(new_c3,4))
          + "*z = " + str(round(new_d3,4)) + "\n")
    p()
    
    print("\n" + "="*32)
    print("STEP 3: SOLVE 2x2 SYSTEM FOR Y,Z")
    print("="*32 + "\n")
    
    if new_b2==0:
        print("Cannot solve")
        p()
        return
    
    m5=new_b3
    m6=new_b2
    
    final_c=new_c3*m5-new_c2*m6
    final_d=new_d3*m5-new_d2*m6
    
    print(str(round(final_c,4)) + "*z = " + str(round(final_d,4)))
    
    if final_c==0:
        print("No unique solution")
        p()
        return
    
    z=final_d/final_c
    print("z = " + str(round(z,4)) + "\n")
    p()
    
    print("\n" + "="*32)
    print("STEP 4: BACK SUBSTITUTION")
    print("="*32 + "\n")
    
    y=(new_d2-new_c2*z)/new_b2
    x=(d1-b1*y-c1*z)/a1
    
    print("y = " + str(round(y,4)))
    print("x = " + str(round(x,4)) + "\n")
    p()
    
    print("\n" + "="*32)
    print("SOLUTION")
    print("="*32 + "\n")
    print("x = " + str(round(x,4)))
    print("y = " + str(round(y,4)))
    print("z = " + str(round(z,4)) + "\n")
    
    print("="*32)
    print("VERIFICATION")
    print("="*32 + "\n")
    eq1=a1*x+b1*y+c1*z
    eq2=a2*x+b2*y+c2*z
    eq3=a3*x+b3*y+c3*z
    print("Eq1: " + str(round(eq1,4)) + " = " + str(d1))
    print("Eq2: " + str(round(eq2,4)) + " = " + str(d2))
    print("Eq3: " + str(round(eq3,4)) + " = " + str(d3) + "\n")
    p()

while True:
    print("\n" + "="*32)
    print("SYSTEM SOLVER")
    print("="*32 + "\n")
    print("2x2 SYSTEMS:")
    print("1 = Substitution method")
    print("2 = Elimination method")
    print("\n3x3 SYSTEMS:")
    print("3 = Substitution method")
    print("4 = Elimination method")
    print("\n5 = Exit\n")
    ch=input("Choose: ")
    
    if ch=="1":
        solve_2x2_subst()
    elif ch=="2":
        solve_2x2_elim()
    elif ch=="3":
        solve_3x3_subst()
    elif ch=="4":
        solve_3x3_elim()
    elif ch=="5":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice.")
