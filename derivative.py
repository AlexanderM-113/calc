import math

def p():
    input("Press EXE...")

def derivative():
    print("\n" + "="*32)
    print("NUMERICAL DERIVATIVE")
    print("="*32 + "\n")
    
    print("Enter function f(x)")
    print("Use: x, +, -, *, /, **, sin, cos, tan")
    print("Example: x**2 + 3*x + 1\n")
    
    func_str=input("f(x) = ")
    x_val=float(input("Find derivative at x = "))
    
    h=0.0001
    
    try:
        f_x_plus_h=eval(func_str.replace('x',str(x_val+h))
                       .replace('sin','math.sin')
                       .replace('cos','math.cos')
                       .replace('tan','math.tan'))
        f_x_minus_h=eval(func_str.replace('x',str(x_val-h))
                        .replace('sin','math.sin')
                        .replace('cos','math.cos')
                        .replace('tan','math.tan'))
    except:
        print("\nError in function")
        p()
        return
    
    derivative_val=(f_x_plus_h-f_x_minus_h)/(2*h)
    
    try:
        f_x=eval(func_str.replace('x',str(x_val))
                .replace('sin','math.sin')
                .replace('cos','math.cos')
                .replace('tan','math.tan'))
    except:
        f_x=0
    
    print("\n" + "="*32)
    print("RESULT")
    print("="*32 + "\n")
    print("f(x) = " + func_str)
    print("At x = " + str(x_val))
    print("f(" + str(x_val) + ") = " + str(round(f_x,4)))
    print("f'(" + str(x_val) + ") = " + str(round(derivative_val,4)) + "\n")
    
    print("="*32)
    print("TANGENT LINE")
    print("="*32 + "\n")
    print("y - y0 = m(x - x0)")
    print("y - " + str(round(f_x,4)) + " = " + str(round(derivative_val,4))
          + "(x - " + str(x_val) + ")")
    
    b=f_x-derivative_val*x_val
    print("\ny = " + str(round(derivative_val,4)) + "*x + " 
          + str(round(b,4)) + "\n")
    p()

while True:
    print("\n" + "="*32)
    print("DERIVATIVE CALCULATOR")
    print("="*32 + "\n")
    print("1 = Calculate derivative")
    print("2 = Exit\n")
    ch=input("Choose: ")
    
    if ch=="1":
        derivative()
    elif ch=="2":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice.")
