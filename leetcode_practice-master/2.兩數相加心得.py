import copy
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
b=3
a=b
print('id(a)',id(a),'id(b)',id(b))
b=5
print('id(a)',id(a),'id(b)',id(b))
l=ListNode(1)
a=l
print('id( l )',id(l),'id(a)',id(a))
l.next=ListNode(2)
print('id( l )',id(l),'id(a)',id(a))
print('a.next',a.next.val)
a=[1,2,3]
b=a
print('b',b)
a.append(4)
print('b',b)
b=copy.copy(a)
a.append(4)
print(a)
print(b)
a=l
l=ListNode(100)
print(a.val)
a=[1,2,3]
b=a
a=[3,2,1]
print(b)
print(id(a[:]),id(a))
a[:]=[5,6,7]
print(a)
a=[1,2,3]
b=a
a[:]=[4,5,6]
print(b)#[4,5,6]