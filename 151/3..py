class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        a=0
        for i in len(l):
            a+=l[i]
            if a==0:
                res=l[:i+1]
                break
        b=ListNode(0)
        a=b
        for i in res:
            a.next=ListNode(i)
            a=a.next
        return b.next

Solution().removeZeroSumSublists()