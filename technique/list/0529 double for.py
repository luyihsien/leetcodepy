a=[1,2,3,4]

for i in range(len(a)):
    print('i',i,'a[i]',a[i])
    for j in range(i+1,len(a)):
        print('j',j,'a[j]',a[j])

for i in range(5,4,-1):
    print(i)#5
for i in range(5,4):
    print('h')#什麼都沒印出來
'''沒這種用法
for i in a:
    for j in a+1:
        
'''