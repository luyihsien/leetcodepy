a=[3,4,1,5,6,7,9,8,10,14,13,12,11]
n=len(a)
for i in reversed(range(n)):#從n-1至0
    for j in range(i):#0至n-1-1為n-2
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)
