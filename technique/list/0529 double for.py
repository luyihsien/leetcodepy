a=[1,2,3,4]
for i in range(len(a)):
    print('i',i,'a[i]',a[i])
    for j in range(i+1,len(a)):
        print('j',j,'a[j]',a[j])
