import math

def p():
    input("Press EXE...")

def centripetal():
    print("\n" + "="*32)
    print("CENTRIPETAL FORCE")
    print("="*32 + "\n")
    print("Formula: Fc = m*v^2/r\n")
    
    m=float(input("Mass (kg): "))
    v=float(input("Velocity (m/s): "))
    r=float(input("Radius (m): "))
    
    fc=m*v*v/r
    
    print("\nFc = " + str(m) + "*" + str(v) + "^2/" + str(r))
    print("Fc = " + str(round(fc,4)) + " N\n")
    p()

def angular_velocity():
    print("\n" + "="*32)
    print("ANGULAR VELOCITY")
    print("="*32 + "\n")
    print("Formula: w = v/r\n")
    
    v=float(input("Velocity (m/s): "))
    r=float(input("Radius (m): "))
    
    w=v/r
    
    print("\nw = " + str(v) + "/" + str(r))
    print("w = " + str(round(w,4)) + " rad/s\n")
    p()

def period():
    print("\n" + "="*32)
    print("PERIOD")
    print("="*32 + "\n")
    print("Formula: T = 2*pi*r/v\n")
    
    r=float(input("Radius (m): "))
    v=float(input("Velocity (m/s): "))
    
    t=2*3.14159*r/v
    f=1/t
    
    print("\nT = 2*3.14159*" + str(r) + "/" + str(v))
    print("T = " + str(round(t,4)) + " s")
    print("f = " + str(round(f,4)) + " Hz\n")
    p()

while True:
    print("\n" + "="*32)
    print("CIRCULAR MOTION")
    print("="*32 + "\n")
    print("1 = Centripetal force")
    print("2 = Angular velocity")
    print("3 = Period/Frequency")
    print("4 = Exit\n")
    ch=input("Choose: ")
    
    if ch=="1":
        centripetal()
    elif ch=="2":
        angular_velocity()
    elif ch=="3":
        period()
    elif ch=="4":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice.")
