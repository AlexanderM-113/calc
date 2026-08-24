def p():
    input("Press EXE...")

def mean(data):
    return sum(data)/len(data)

def median(data):
    sorted_d=sorted(data)
    n=len(data)
    if n%2==0:
        return (sorted_d[n//2-1]+sorted_d[n//2])/2
    else:
        return sorted_d[n//2]

def mode(data):
    counts={}
    for x in data:
        counts[x]=counts.get(x,0)+1
    if not counts:
        return None
    return max(counts,key=counts.get)

def stdev(data):
    m=mean(data)
    var=sum((x-m)**2 for x in data)/len(data)
    return var**0.5

def stats():
    print("\n" + "="*32)
    print("STATISTICS")
    print("="*32 + "\n")
    print("Enter data (space-separated)\n")
    
    data_str=input("Data: ")
    data=[float(x) for x in data_str.split()]
    
    m=mean(data)
    med=median(data)
    mod=mode(data)
    sd=stdev(data)
    
    print("\n" + "="*32)
    print("RESULTS")
    print("="*32 + "\n")
    print("n = " + str(len(data)))
    print("Mean = " + str(round(m,4)))
    print("Median = " + str(round(med,4)))
    print("Mode = " + str(mod))
    print("Std Dev = " + str(round(sd,4)))
    print("Min = " + str(min(data)))
    print("Max = " + str(max(data)))
    print("Range = " + str(max(data)-min(data)) + "\n")
    p()

def linear_regression():
    print("\n" + "="*32)
    print("LINEAR REGRESSION")
    print("="*32 + "\n")
    print("Enter x values (space-separated)")
    x_str=input("x: ")
    x=[float(v) for v in x_str.split()]
    
    print("Enter y values (space-separated)")
    y_str=input("y: ")
    y=[float(v) for v in y_str.split()]
    
    if len(x)!=len(y):
        print("\nError: same number of x and y")
        p()
        return
    
    n=len(x)
    x_mean=sum(x)/n
    y_mean=sum(y)/n
    
    num=sum((x[i]-x_mean)*(y[i]-y_mean) for i in range(n))
    den=sum((x[i]-x_mean)**2 for i in range(n))
    
    if den==0:
        print("\nError: no x variation")
        p()
        return
    
    slope=num/den
    intercept=y_mean-slope*x_mean
    
    r_num=sum((x[i]-x_mean)*(y[i]-y_mean) for i in range(n))
    r_den=(sum((x[i]-x_mean)**2 for i in range(n))*
           sum((y[i]-y_mean)**2 for i in range(n)))**0.5
    r=r_num/r_den if r_den!=0 else 0
    
    print("\n" + "="*32)
    print("REGRESSION LINE")
    print("="*32 + "\n")
    print("y = " + str(round(slope,4)) + "*x + " 
          + str(round(intercept,4)))
    print("\nCorrelation (r) = " + str(round(r,4)))
    print("R-squared = " + str(round(r*r,4)) + "\n")
    p()

while True:
    print("\n" + "="*32)
    print("STATISTICS SUITE")
    print("="*32 + "\n")
    print("1 = Descriptive stats")
    print("2 = Linear regression")
    print("3 = Exit\n")
    ch=input("Choose: ")
    
    if ch=="1":
        stats()
    elif ch=="2":
        linear_regression()
    elif ch=="3":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice.")
