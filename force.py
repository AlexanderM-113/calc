import math

def p():
    input("Press EXE...")

def force():
    print("\n" + "="*32)
    print("FORCE (F = ma)")
    print("="*32 + "\n")
    
    print("1 = Find force")
    print("2 = Find mass")
    print("3 = Find acceleration\n")
    
    ch=input("Choose: ")
    
    if ch=="1":
        m=float(input("Mass (kg): "))
        a=float(input("Acceleration (m/s^2): "))
        f=m*a
        print("\nF = m*a")
        print("F = " + str(m) + "*" + str(a))
        print("F = " + str(round(f,4)) + " N\n")
    
    elif ch=="2":
        f=float(input("Force (N): "))
        a=float(input("Acceleration (m/s^2): "))
        if a==0:
            print("\nError: acceleration cannot be 0")
            p()
            return
        m=f/a
        print("\nm = F/a")
        print("m = " + str(f) + "/" + str(a))
        print("m = " + str(round(m,4)) + " kg\n")
    
    elif ch=="3":
        f=float(input("Force (N): "))
        m=float(input("Mass (kg): "))
        if m==0:
            print("\nError: mass cannot be 0")
            p()
            return
        a=f/m
        print("\na = F/m")
        print("a = " + str(f) + "/" + str(m))
        print("a = " + str(round(a,4)) + " m/s^2\n")
    
    p()

def momentum():
    print("\n" + "="*32)
    print("MOMENTUM (p = mv)")
    print("="*32 + "\n")
    
    print("1 = Find momentum")
    print("2 = Find mass")
    print("3 = Find velocity\n")
    
    ch=input("Choose: ")
    
    if ch=="1":
        m=float(input("Mass (kg): "))
        v=float(input("Velocity (m/s): "))
        p=m*v
        print("\np = m*v")
        print("p = " + str(m) + "*" + str(v))
        print("p = " + str(round(p,4)) + " kg*m/s\n")
    
    elif ch=="2":
        p=float(input("Momentum (kg*m/s): "))
        v=float(input("Velocity (m/s): "))
        if v==0:
            print("\nError: velocity cannot be 0")
            p()
            return
        m=p/v
        print("\nm = p/v")
        print("m = " + str(p) + "/" + str(v))
        print("m = " + str(round(m,4)) + " kg\n")
    
    elif ch=="3":
        p=float(input("Momentum (kg*m/s): "))
        m=float(input("Mass (kg): "))
        if m==0:
            print("\nError: mass cannot be 0")
            p()
            return
        v=p/m
        print("\nv = p/m")
        print("v = " + str(p) + "/" + str(m))
        print("v = " + str(round(v,4)) + " m/s\n")
    
    p()

def impulse():
    print("\n" + "="*32)
    print("IMPULSE (J = F*t)")
    print("="*32 + "\n")
    
    f=float(input("Force (N): "))
    t=float(input("Time (s): "))
    j=f*t
    
    print("\nJ = F*t")
    print("J = " + str(f) + "*" + str(t))
    print("J = " + str(round(j,4)) + " N*s")
    print("\nChange in momentum = " + str(round(j,4)) + " kg*m/s\n")
    p()

def collision():
    print("\n" + "="*32)
    print("COLLISION (Conservation)")
    print("="*32 + "\n")
    print("p1 + p2 = p1' + p2'\n")
    
    m1=float(input("Mass 1 (kg): "))
    v1=float(input("Velocity 1 (m/s): "))
    m2=float(input("Mass 2 (kg): "))
    v2=float(input("Velocity 2 (m/s): "))
    
    p_before=m1*v1+m2*v2
    
    print("\nMomentum before:")
    print("p = m1*v1 + m2*v2")
    print("p = " + str(m1) + "*" + str(v1))
    print("  + " + str(m2) + "*" + str(v2))
    print("p = " + str(round(p_before,4)) + " kg*m/s")
    
    print("\nIf objects stick together:")
    v_final=p_before/(m1+m2)
    print("v_final = p/(m1+m2)")
    print("v_final = " + str(round(v_final,4)) + " m/s\n")
    p()

while True:
    print("\n" + "="*32)
    print("FORCE/MOMENTUM CALCULATOR")
    print("="*32 + "\n")
    print("1 = Force (F = ma)")
    print("2 = Momentum (p = mv)")
    print("3 = Impulse (J = F*t)")
    print("4 = Collision analysis")
    print("5 = Exit\n")
    ch=input("Choose: ")
    
    if ch=="1":
        force()
    elif ch=="2":
        momentum()
    elif ch=="3":
        impulse()
    elif ch=="4":
        collision()
    elif ch=="5":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice.")
