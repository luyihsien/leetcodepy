a=[1,2,3,4,5]
a[3:].reverse()#TypeError: can only assign an iterable
print(a)#[1, 2, 3, 4, 5]
a[3:][::-1]
print(a)#[1, 2, 3, 4, 5]
reversed(a[3:])#None
#36-44陳述同一件事
a = [1, 2, 3]
b = a
del a[:]
print(b)#[]

a = [1, 2, 3]
b = a
a = []
print(b)#[1, 2, 3]
a=[1,2,3]
b=a
b=[]
del b[:]
print(a)#皆[1,2,3] 因是b指針指向a不是a指針指向b
a=[3,2,1]
b=a
a[:].reverse()
print(a)#[3,2,1]#沒reverse a
print(b)#[3,2,1]
b=a
a.reverse()
print(a)
print(b)
a=[3,2,1]
b=a
a=[1,2,3]
print(a)
print(b)
c=[4,5,6]
d=[4,5,6]
del c[:]
print(c)
print(d)