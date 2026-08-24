import math

def p():
    input("Press EXE...")

def trapezoidal():
    print("\n" + "="*32)
    print("TRAPEZOIDAL RULE")
    print("="*32 + "\n")
    
    print("Enter function f(x)")
    print("Use: x, +, -, *, /, **, sin, cos\n")
    
    func_str=input("f(x) = ")
    a=float(input("Lower limit (a): "))
    b=float(input("Upper limit (b): "))
    n=int(input("Number of intervals: "))
    
    h=(b-a)/n
    total=0
    
    try:
        f_a=eval(func_str.replace('x',str(a))
                 .replace('sin','math.sin')
                 .replace('cos','math.cos'))
        f_b=eval(func_str.replace('x',str(b))
                 .replace('sin','math.sin')
                 .replace('cos','math.cos'))
    except:
        print("\nError in function")
        p()
        return
    
    total=f_a+f_b
    
    for i in range(1,n):
        x=a+i*h
        try:
            fx=eval(func_str.replace('x',str(x))
                   .replace('sin','math.sin')
                   .replace('cos','math.cos'))
            total+=2*fx
        except:
            pass
    
    integral=h*total/2
    
    print("\n" + "="*32)
    print("RESULT")
    print("="*32 + "\n")
    print("f(x) = " + func_str)
    print("Integral from " + str(a) + " to " + str(b))
    print("Intervals: " + str(n))
    print("Step size (h): " + str(round(h,4)))
    print("\nIntegral = " + str(round(integral,6)) + "\n")
    p()

def simpson():
    print("\n" + "="*32)
    print("SIMPSON'S RULE")
    print("="*32 + "\n")
    
    print("Enter function f(x)\n")
    func_str=input("f(x) = ")
    a=float(input("Lower limit (a): "))
    b=float(input("Upper limit (b): "))
    n=int(input("Number of intervals (even): "))
    
    if n%2!=0:
        n+=1
        print("Adjusted to " + str(n))
    
    h=(b-a)/n
    
    try:
        f_a=eval(func_str.replace('x',str(a))
                 .replace('sin','math.sin')
                 .replace('cos','math.cos'))
        f_b=eval(func_str.replace('x',str(b))
                 .replace('sin','math.sin')
                 .replace('cos','math.cos'))
    except:
        print("\nError in function")
        p()
        return
    
    total=f_a+f_b
    
    for i in range(1,n):
        x=a+i*h
        try:
            fx=eval(func_str.replace('x',str(x))
                   .replace('sin','math.sin')
                   .replace('cos','math.cos'))
            if i%2==0:
                total+=2*fx
            else:
                total+=4*fx
        except:
            pass
    
    integral=h*total/3
    
    print("\n" + "="*32)
    print("RESULT")
    print("="*32 + "\n")
    print("f(x) = " + func_str)
    print("Integral from " + str(a) + " to " + str(b))
    print("Intervals: " + str(n))
    print("\nIntegral = " + str(round(integral,6)) + "\n")
    p()

while True:
    print("\n" + "="*32)
    print("INTEGRATION APPROXIMATOR")
    print("="*32 + "\n")
    print("1 = Trapezoidal rule")
    print("2 = Simpson's rule")
    print("3 = Exit\n")
    ch=input("Choose: ")
    
    if ch=="1":
        trapezoidal()
    elif ch=="2":
        simpson()
    elif ch=="3":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice.")
