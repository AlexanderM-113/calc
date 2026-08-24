import math

def p():
    input("Press EXE...")

def solve_sss():
    print("\n" + "="*32)
    print("SOLVE: 3 SIDES (SSS)")
    print("="*32 + "\n")
    
    a=float(input("Side a: "))
    b=float(input("Side b: "))
    c=float(input("Side c: "))
    
    if a+b<=c or a+c<=b or b+c<=a:
        print("\nInvalid triangle (triangle inequality)")
        p()
        return
    
    cos_A=(b*b+c*c-a*a)/(2*b*c)
    cos_B=(a*a+c*c-b*b)/(2*a*c)
    cos_C=(a*a+b*b-c*c)/(2*a*b)
    
    A=math.acos(cos_A)*180/math.pi
    B=math.acos(cos_B)*180/math.pi
    C=180-A-B
    
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    
    print("\n" + "="*32)
    print("ANGLES (Law of Cosines)")
    print("="*32 + "\n")
    print("Angle A: " + str(round(A,2)) + " deg")
    print("Angle B: " + str(round(B,2)) + " deg")
    print("Angle C: " + str(round(C,2)) + " deg")
    print("Sum: " + str(round(A+B+C,2)) + " deg\n")
    
    print("="*32)
    print("AREA (Heron's Formula)")
    print("="*32 + "\n")
    print("s = (a+b+c)/2 = " + str(round(s,4)))
    print("A = sqrt(s(s-a)(s-b)(s-c))")
    print("A = " + str(round(area,4)) + "\n")
    p()

def solve_sas():
    print("\n" + "="*32)
    print("SOLVE: 2 SIDES + ANGLE (SAS)")
    print("="*32 + "\n")
    
    a=float(input("Side a: "))
    b=float(input("Side b: "))
    C_deg=float(input("Angle C (deg): "))
    
    C=C_deg*math.pi/180
    c_sq=a*a+b*b-2*a*b*math.cos(C)
    c=math.sqrt(c_sq)
    
    sin_A=a*math.sin(C)/c
    sin_B=b*math.sin(C)/c
    
    A=math.asin(sin_A)*180/math.pi
    B=180-A-C_deg
    
    print("\n" + "="*32)
    print("RESULTS")
    print("="*32 + "\n")
    print("Side c: " + str(round(c,4)))
    print("Angle A: " + str(round(A,2)) + " deg")
    print("Angle B: " + str(round(B,2)) + " deg\n")
    
    area=0.5*a*b*math.sin(C)
    print("Area: " + str(round(area,4)) + "\n")
    p()

def solve_asa():
    print("\n" + "="*32)
    print("SOLVE: 2 ANGLES + SIDE (ASA)")
    print("="*32 + "\n")
    
    A_deg=float(input("Angle A (deg): "))
    B_deg=float(input("Angle B (deg): "))
    c=float(input("Side c: "))
    
    C_deg=180-A_deg-B_deg
    
    if C_deg<=0:
        print("\nInvalid angles")
        p()
        return
    
    A=A_deg*math.pi/180
    B=B_deg*math.pi/180
    C=C_deg*math.pi/180
    
    a=c*math.sin(A)/math.sin(C)
    b=c*math.sin(B)/math.sin(C)
    
    print("\n" + "="*32)
    print("RESULTS")
    print("="*32 + "\n")
    print("Side a: " + str(round(a,4)))
    print("Side b: " + str(round(b,4)))
    print("Angle C: " + str(round(C_deg,2)) + " deg\n")
    
    area=0.5*a*b*math.sin(C)
    print("Area: " + str(round(area,4)) + "\n")
    p()

while True:
    print("\n" + "="*32)
    print("TRIANGLE SOLVER")
    print("="*32 + "\n")
    print("1 = 3 Sides (SSS)")
    print("2 = 2 Sides+Angle (SAS)")
    print("3 = 2 Angles+Side (ASA)")
    print("4 = Exit\n")
    ch=input("Choose: ")
    
    if ch=="1":
        solve_sss()
    elif ch=="2":
        solve_sas()
    elif ch=="3":
        solve_asa()
    elif ch=="4":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice.")
