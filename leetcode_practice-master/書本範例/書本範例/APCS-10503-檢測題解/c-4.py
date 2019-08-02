#1050305-4

a=[];b=[]
b.append(0)
for i in range(1,101):
    b.append(i)

print(b,"\n")
    
a.append(0)
for i in range(1,101):
    a.append(i)
    a[i]=b[i]+a[i-1]
print(a)

print(a[50],a[30])
print("%d\n" %(a[50]-a[30]))


