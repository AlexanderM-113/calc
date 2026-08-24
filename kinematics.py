import math

def p():
    input("Press EXE...")

def constant_accel():
    print("\n" + "="*32)
    print("CONSTANT ACCELERATION")
    print("="*32 + "\n")
    print("Equations of motion:\n")
    print("1 = Find final velocity")
    print("2 = Find displacement")
    print("3 = Find acceleration")
    print("4 = Find time\n")
    
    ch=input("Choose: ")
    
    if ch=="1":
        v0=float(input("Initial velocity (m/s): "))
        a=float(input("Acceleration (m/s^2): "))
        t=float(input("Time (s): "))
        vf=v0+a*t
        print("\nvf = v0 + at")
        print("vf = " + str(v0) + " + " + str(a) + "*" + str(t))
        print("vf = " + str(round(vf,4)) + " m/s\n")
    
    elif ch=="2":
        v0=float(input("Initial velocity (m/s): "))
        a=float(input("Acceleration (m/s^2): "))
        t=float(input("Time (s): "))
        d=v0*t+0.5*a*t*t
        print("\nd = v0*t + 0.5*a*t^2")
        print("d = " + str(v0) + "*" + str(t))
        print("  + 0.5*" + str(a) + "*" + str(t) + "^2")
        print("d = " + str(round(d,4)) + " m\n")
    
    elif ch=="3":
        vf=float(input("Final velocity (m/s): "))
        v0=float(input("Initial velocity (m/s): "))
        t=float(input("Time (s): "))
        if t==0:
            print("\nError: time cannot be 0")
            p()
            return
        a=(vf-v0)/t
        print("\na = (vf - v0)/t")
        print("a = (" + str(vf) + " - " + str(v0) + ")/" + str(t))
        print("a = " + str(round(a,4)) + " m/s^2\n")
    
    elif ch=="4":
        vf=float(input("Final velocity (m/s): "))
        v0=float(input("Initial velocity (m/s): "))
        a=float(input("Acceleration (m/s^2): "))
        if a==0:
            print("\nError: acceleration cannot be 0")
            p()
            return
        t=(vf-v0)/a
        print("\nt = (vf - v0)/a")
        print("t = (" + str(vf) + " - " + str(v0) + ")/" + str(a))
        print("t = " + str(round(t,4)) + " s\n")
    
    p()

def projectile():
    print("\n" + "="*32)
    print("PROJECTILE MOTION")
    print("="*32 + "\n")
    
    v0=float(input("Initial velocity (m/s): "))
    theta=float(input("Angle (degrees): "))
    theta_rad=theta*math.pi/180
    
    vx=v0*math.cos(theta_rad)
    vy=v0*math.sin(theta_rad)
    
    t_max=vy/9.81
    y_max=vy*vy/(2*9.81)
    t_total=2*t_max
    x_range=vx*t_total
    
    print("\n" + "="*32)
    print("RESULTS")
    print("="*32 + "\n")
    print("vx = " + str(round(vx,4)) + " m/s")
    print("vy = " + str(round(vy,4)) + " m/s")
    print("\nMax height: " + str(round(y_max,4)) + " m")
    print("Time to max height: " + str(round(t_max,4)) + " s")
    print("Total flight time: " + str(round(t_total,4)) + " s")
    print("Range: " + str(round(x_range,4)) + " m\n")
    p()

def free_fall():
    print("\n" + "="*32)
    print("FREE FALL")
    print("="*32 + "\n")
    print("g = 9.81 m/s^2\n")
    
    print("1 = Find final velocity")
    print("2 = Find distance fallen")
    print("3 = Find time to fall\n")
    
    ch=input("Choose: ")
    
    if ch=="1":
        t=float(input("Time (s): "))
        vf=9.81*t
        print("\nvf = g*t")
        print("vf = 9.81*" + str(t))
        print("vf = " + str(round(vf,4)) + " m/s\n")
    
    elif ch=="2":
        t=float(input("Time (s): "))
        d=0.5*9.81*t*t
        print("\nd = 0.5*g*t^2")
        print("d = 0.5*9.81*" + str(t) + "^2")
        print("d = " + str(round(d,4)) + " m\n")
    
    elif ch=="3":
        d=float(input("Distance (m): "))
        t=math.sqrt(2*d/9.81)
        print("\nt = sqrt(2*d/g)")
        print("t = sqrt(2*" + str(d) + "/9.81)")
        print("t = " + str(round(t,4)) + " s\n")
    
    p()

while True:
    print("\n" + "="*32)
    print("KINEMATICS SOLVER")
    print("="*32 + "\n")
    print("1 = Constant acceleration")
    print("2 = Projectile motion")
    print("3 = Free fall")
    print("4 = Exit\n")
    ch=input("Choose: ")
    
    if ch=="1":
        constant_accel()
    elif ch=="2":
        projectile()
    elif ch=="3":
        free_fall()
    elif ch=="4":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice.")
