a=[1,2,3]
print(id(a))
a[:]=a[1:]
print(a)
print(id(a))
a.sort()
