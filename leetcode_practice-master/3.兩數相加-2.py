import sys
b=[1,2,3]
a=b
#b=[1,2,3]#指向不同的[1,2,3]
b.append(4)
print(a)#多了第三列則[1,2,3]，無則[1,2,3,4]

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
a=ListNode(1)
print(id(a))
print('getsizeof a',sys.getsizeof(a))
print(id(a.val))
print(id(a.next))
a.next=ListNode(2)
print(id(a))
print('getsizeof a',sys.getsizeof(a))
print(id(a.next))
a.next.next=ListNode(3)
print(id(a))
print('getsizeof a',sys.getsizeof(a))
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = None
        dummy = p#就一直是None，也不會跟著跑動。
        tmp = 0
        while l1 and l2:
            tmp = l1.val + l2.val + tmp // 10
            p = ListNode(tmp % 10)
            print(p.val)
            l1 = l1.next
            l2 = l2.next
            p = p.next
            print('dummy',dummy)
        while l1:
            tmp = l1.val + tmp // 10
            p = ListNode(tmp % 10)
            l1 = l1.next
            p = p.next
        while l2:
            tmp = l2.val + tmp // 10
            p = ListNode(tmp % 10)
            l2 = l2.next
            p = p.next
        if tmp // 10:
            p = ListNode(tmp // 10)
        print(dummy)
        return dummy
l1=ListNode(5)
l1.next=ListNode(6)
l1.next.next=ListNode(4)
l2=ListNode(2)
l2.next=ListNode(4)
l2.next.next=ListNode(3)
print(Solution().addTwoNumbers(l1,l2))
a=ListNode(4)
b=a
a=ListNode(5)
print(b.val)
a=[]
print('getsizeof a',sys.getsizeof(a),'id',id(a))
a.append(1)
print('getsizeof a',sys.getsizeof(a),'id',id(a))
a.append(2)
print('getsizeof a',sys.getsizeof(a),'id',id(a))
a.append(3)
print('getsizeof a',sys.getsizeof(a),'id',id(a))
a.append(4)
print('getsizeof a',sys.getsizeof(a),'id',id(a))
''''
getsizeof a 64 id 2624454943368
getsizeof a 96 id 2624454943368
getsizeof a 96 id 2624454943368
getsizeof a 96 id 2624454943368
getsizeof a 96 id 2624454943368
'''