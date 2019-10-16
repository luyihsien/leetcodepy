#20191016
print(min(set([1,2,3,4])))#1
l=[{1,2,3,4},{5,6,7,8,2},{9,10,11,12,2}]
a=l[0]
print(a)
for i in range(len(l)-1):
    a&=l[i+1]
    print(a)
print(min(a))


