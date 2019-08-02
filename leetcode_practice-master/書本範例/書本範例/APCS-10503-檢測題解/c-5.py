#1050305-5

def f(n,c):
    sum=0
    if n<2 : return 0
    
    print("n=",n);print("c=",c)
    for i in range(1,n+1):
        sum =sum + i
        c += 1
    n=int(2*n/3)
    
    sum += f(n,c)
    return sum

#main
f(1000,0)
