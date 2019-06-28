def Hamoi(n,a,b,c):
    if n==0:
        return
    else:
        Hamoi(n-1,a,c,b)
        print("{}->{}".format(a,c))
        Hamoi(n-1,b,a,c)
Hamoi(3,'a','b','c')