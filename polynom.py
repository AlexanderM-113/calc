def p():
    input("Press EXE...")

def poly_div():
    print("\n" + "="*32)
    print("POLYNOMIAL LONG DIVISION")
    print("="*32 + "\n")
    print("Enter dividend (numerator)")
    print("Format: coefficient of each term")
    print("Example: x^3+2x^2-3x+1")
    print("Enter: 1 2 -3 1\n")
    
    div_str=input("Dividend: ")
    dividend=[float(x) for x in div_str.split()]
    
    print("\nEnter divisor (denominator)")
    print("Example: x-1")
    print("Enter: 1 -1\n")
    
    div_str2=input("Divisor: ")
    divisor=[float(x) for x in div_str2.split()]
    
    if len(divisor)==0 or divisor[0]==0:
        print("Invalid divisor")
        p()
        return
    
    print("\n" + "="*32)
    print("DIVISION STEPS")
    print("="*32 + "\n")
    
    quot=[]
    rem=dividend[:]
    divisor_len=len(divisor)
    dividend_len=len(dividend)
    
    for i in range(dividend_len-divisor_len+1):
        coeff=rem[i]/divisor[0]
        quot.append(coeff)
        print("Step " + str(i+1) + ": " + str(round(coeff,2)))
        
        for j in range(divisor_len):
            rem[i+j]-=coeff*divisor[j]
        
        rem.pop(i)
    
    rem=[x for x in rem if abs(x)>0.0001]
    
    print("\n" + "="*32)
    print("QUOTIENT")
    print("="*32 + "\n")
    print("Coefficients: " + str([round(x,4) for x in quot]))
    
    print("\n" + "="*32)
    print("REMAINDER")
    print("="*32 + "\n")
    if len(rem)==0:
        print("0 (divides evenly)")
    else:
        print("Coefficients: " + str([round(x,4) for x in rem]))
    
    print()
    p()

while True:
    print("\n" + "="*32)
    print("POLYNOMIAL DIVISION")
    print("="*32 + "\n")
    print("1 = Perform division")
    print("2 = Exit\n")
    ch=input("Choose: ")
    
    if ch=="1":
        poly_div()
    elif ch=="2":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice.")
