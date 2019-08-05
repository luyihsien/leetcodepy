for _ in range(5):
    print(_)
num=[9,6,1,6,2]
n=len(num)
a=[float('inf')]+num+[float('inf')]
print(a)
b=[]
c=[]
for i in range(1,n+1,2):
    b.append(max(0,a[i]+1-min(a[i-1],a[i+1])))
    print(sum(b))
for i in range(2,n+1,2):
    c.append(max(0,a[i]+1-min(a[i-1],a[i+1])))
    print(c)
print(None if None else 4)
def x(n):
    if n==1:
        return 1
    else:
        return x(n-1)
print(x(10))
i=0
print(i if i else 1)#1
x=6
y=6
print(x is y)
a=[1,2,3]
b=a.copy()
print(a==b)#True
print(a is b)#False

