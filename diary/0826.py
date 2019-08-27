import sys
a=[1,2,3,4]
print(id(a))
b=a
b=b+[5]
b.append(5)
print(a,id(a))
print(b,id(b))
a=5
b=a
print(id(a),id(b))
b+=1
print(id(b))
print(id(a))
print(a,b)
class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
a=ListNode(5)
b=a
print(sys.getsizeof(a))
print(sys.getsizeof(a.val))
print(sys.getsizeof(a.next))
b.next=ListNode(400000)
print(sys.getsizeof(a))
print(sys.getsizeof(a.next.val))
b=b.next
print('b',sys.getsizeof(b))
b.next=ListNode(3000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
print(sys.getsizeof(a))
a=100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
print(sys.getsizeof(a))
a=1000#與a=1同
print(sys.getsizeof(a))