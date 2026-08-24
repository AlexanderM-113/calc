def p():
    input("Press EXE...")

def kinetic():
    print("\n" + "="*32)
    print("KINETIC ENERGY")
    print("="*32 + "\n")
    print("Formula: KE = 0.5*m*v^2\n")
    
    m=float(input("Mass (kg): "))
    v=float(input("Velocity (m/s): "))
    
    ke=0.5*m*v*v
    
    print("\nKE = 0.5*" + str(m) + "*" + str(v) + "^2")
    print("KE = " + str(round(ke,4)) + " J\n")
    p()

def potential():
    print("\n" + "="*32)
    print("GRAVITATIONAL POTENTIAL ENERGY")
    print("="*32 + "\n")
    print("Formula: PE = m*g*h\n")
    
    m=float(input("Mass (kg): "))
    h=float(input("Height (m): "))
    g=9.81
    
    pe=m*g*h
    
    print("\nPE = " + str(m) + "*9.81*" + str(h))
    print("PE = " + str(round(pe,4)) + " J\n")
    p()

def elastic():
    print("\n" + "="*32)
    print("ELASTIC POTENTIAL ENERGY")
    print("="*32 + "\n")
    print("Formula: PE = 0.5*k*x^2\n")
    
    k=float(input("Spring constant (N/m): "))
    x=float(input("Displacement (m): "))
    
    pe=0.5*k*x*x
    
    print("\nPE = 0.5*" + str(k) + "*" + str(x) + "^2")
    print("PE = " + str(round(pe,4)) + " J\n")
    p()

def work():
    print("\n" + "="*32)
    print("WORK")
    print("="*32 + "\n")
    print("Formula: W = F*d*cos(theta)\n")
    
    f=float(input("Force (N): "))
    d=float(input("Distance (m): "))
    theta=float(input("Angle (degrees): "))
    
    import math
    theta_rad=theta*math.pi/180
    w=f*d*math.cos(theta_rad)
    
    print("\nW = " + str(f) + "*" + str(d) + "*cos(" + str(theta) + ")")
    print("W = " + str(round(w,4)) + " J\n")
    p()

def power():
    print("\n" + "="*32)
    print("POWER")
    print("="*32 + "\n")
    print("Formula: P = W/t\n")
    
    print("1 = Find power")
    print("2 = Find work")
    print("3 = Find time\n")
    
    ch=input("Choose: ")
    
    if ch=="1":
        w=float(input("Work (J): "))
        t=float(input("Time (s): "))
        p_val=w/t
        print("\nP = " + str(w) + "/" + str(t))
        print("P = " + str(round(p_val,4)) + " W\n")
    
    elif ch=="2":
        p_val=float(input("Power (W): "))
        t=float(input("Time (s): "))
        w=p_val*t
        print("\nW = P*t")
        print("W = " + str(p_val) + "*" + str(t))
        print("W = " + str(round(w,4)) + " J\n")
    
    elif ch=="3":
        w=float(input("Work (J): "))
        p_val=float(input("Power (W): "))
        if p_val==0:
            print("\nError: power cannot be 0")
            p()
            return
        t=w/p_val
        print("\nt = W/P")
        print("t = " + str(w) + "/" + str(p_val))
        print("t = " + str(round(t,4)) + " s\n")
    
    p()

def energy_conservation():
    print("\n" + "="*32)
    print("ENERGY CONSERVATION")
    print("="*32 + "\n")
    print("KE + PE = constant\n")
    
    ke1=float(input("Initial KE (J): "))
    pe1=float(input("Initial PE (J): "))
    ke2=float(input("Final KE (J): "))
    
    total_energy=ke1+pe1
    pe2=total_energy-ke2
    
    print("\nInitial Energy: " + str(round(ke1,4))
          + " + " + str(round(pe1,4)))
    print("            = " + str(round(total_energy,4)) + " J")
    print("\nFinal PE = " + str(round(pe2,4)) + " J\n")
    p()

while True:
    print("\n" + "="*32)
    print("ENERGY CALCULATOR")
    print("="*32 + "\n")
    print("1 = Kinetic energy")
    print("2 = Potential energy")
    print("3 = Elastic PE")
    print("4 = Work")
    print("5 = Power")
    print("6 = Energy conservation")
    print("7 = Exit\n")
    ch=input("Choose: ")
    
    if ch=="1":
        kinetic()
    elif ch=="2":
        potential()
    elif ch=="3":
        elastic()
    elif ch=="4":
        work()
    elif ch=="5":
        power()
    elif ch=="6":
        energy_conservation()
    elif ch=="7":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice.")
