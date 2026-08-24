def p():
    input("Press EXE...")

def read_matrix(name,rows,cols):
    print("\nEnter " + name + " (" + str(rows) + "x" + str(cols) + "):")
    m=[]
    for i in range(rows):
        row_str=input("Row " + str(i+1) + ": ")
        row=[float(x) for x in row_str.split()]
        if len(row)!=cols:
            print("Error: need " + str(cols) + " values")
            return None
        m.append(row)
    return m

def print_matrix(m):
    for row in m:
        print(" ".join([str(round(x,4)).rjust(8) for x in row]))

def add_matrices():
    print("\n" + "="*32)
    print("MATRIX ADDITION")
    print("="*32)
    
    r=int(input("\nRows: "))
    c=int(input("Cols: "))
    
    A=read_matrix("Matrix A",r,c)
    if not A:
        return
    B=read_matrix("Matrix B",r,c)
    if not B:
        return
    
    C=[[A[i][j]+B[i][j] for j in range(c)] for i in range(r)]
    
    print("\n" + "="*32)
    print("RESULT: A + B")
    print("="*32 + "\n")
    print_matrix(C)
    print()
    p()

def sub_matrices():
    print("\n" + "="*32)
    print("MATRIX SUBTRACTION")
    print("="*32)
    
    r=int(input("\nRows: "))
    c=int(input("Cols: "))
    
    A=read_matrix("Matrix A",r,c)
    if not A:
        return
    B=read_matrix("Matrix B",r,c)
    if not B:
        return
    
    C=[[A[i][j]-B[i][j] for j in range(c)] for i in range(r)]
    
    print("\n" + "="*32)
    print("RESULT: A - B")
    print("="*32 + "\n")
    print_matrix(C)
    print()
    p()

def mult_matrices():
    print("\n" + "="*32)
    print("MATRIX MULTIPLICATION")
    print("="*32)
    
    r1=int(input("\nMatrix A rows: "))
    c1=int(input("Matrix A cols: "))
    r2=int(input("Matrix B rows: "))
    c2=int(input("Matrix B cols: "))
    
    if c1!=r2:
        print("\nError: A cols must = B rows")
        p()
        return
    
    A=read_matrix("Matrix A",r1,c1)
    if not A:
        return
    B=read_matrix("Matrix B",r2,c2)
    if not B:
        return
    
    C=[[sum(A[i][k]*B[k][j] for k in range(c1))
        for j in range(c2)] for i in range(r1)]
    
    print("\n" + "="*32)
    print("RESULT: A * B (" + str(r1) + "x" + str(c2) + ")")
    print("="*32 + "\n")
    print_matrix(C)
    print()
    p()

def det_2x2(m):
    return m[0][0]*m[1][1]-m[0][1]*m[1][0]

def det_3x3(m):
    d=(m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
       -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
       +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))
    return d

def determinant():
    print("\n" + "="*32)
    print("DETERMINANT")
    print("="*32)
    
    n=int(input("\nMatrix size (2 or 3): "))
    
    if n==2:
        A=read_matrix("Matrix",2,2)
        if not A:
            return
        d=det_2x2(A)
    elif n==3:
        A=read_matrix("Matrix",3,3)
        if not A:
            return
        d=det_3x3(A)
    else:
        print("Only 2x2 or 3x3 supported")
        p()
        return
    
    print("\n" + "="*32)
    print("DETERMINANT = " + str(round(d,4)))
    print("="*32 + "\n")
    p()

while True:
    print("\n" + "="*32)
    print("MATRIX OPERATIONS")
    print("="*32 + "\n")
    print("1 = Add matrices")
    print("2 = Subtract matrices")
    print("3 = Multiply matrices")
    print("4 = Determinant")
    print("5 = Exit\n")
    ch=input("Choose: ")
    
    if ch=="1":
        add_matrices()
    elif ch=="2":
        sub_matrices()
    elif ch=="3":
        mult_matrices()
    elif ch=="4":
        determinant()
    elif ch=="5":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice.")
