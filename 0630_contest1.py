c=7
nu=4
c=10
nu=3
n=[0]*nu
a=0
while c>=0:
    for i in range(len(n)):
        c = c - (a + i+1)
        print('c',c)
        if c>=0:
            n[i]+=a+i+1
        else:
            d=c+(a+i+1)
            n[i]+=d
            break
    a=a+len(n)
print(n)