import collections
l=[1,2,3,4]
a=list(reversed(l))
print(a)
b=l.reverse()#翻轉原本list不會造成存出一個反轉list給b#None
b=reversed(l)
print(b)
print(collections.Counter(b))