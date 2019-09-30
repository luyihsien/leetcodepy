import collections
arr = [-3,0,1,-3,1,1,1,-3,10,0]
c=collections.Counter(arr)
l=[]
for i in c:
    l.append(c[i])
l.sort()
n=len(l)
for i in range(n-1):
    if l[i]==l[i+1]:
        print('False')
print('True')