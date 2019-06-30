c=2
l=14
while 1:
    if c>=l:
        break
    else:
        c=c*2

a=[]
for i in range(1,c+1):
    a.append(i)
print(a)
b=2
while l>=b-1:
    if l>=b-1 and l<2*(b-1):
        a[2*(b-1)-(l-(b-1)):2*(b-1)+1]=a[b-1:l+1][::-1]
        a[l:2*(b-1)-(l-(b-1))+1]=[None]*len(a[l:2*(b-1)-(l-(b-1))+1])

    else:
        a[b-1:2*(b-1)+1]=a[b-1:2*(b-1)+1][::-1]
    b=b*4
print(a)

