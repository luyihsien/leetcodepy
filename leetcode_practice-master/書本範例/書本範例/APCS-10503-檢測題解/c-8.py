#1050305-8

a,b=0,1
N=10

for i in range(2,N+1):
    temp=b
    b=a+b
    a=temp
    print("%d" %b,end=" ")




