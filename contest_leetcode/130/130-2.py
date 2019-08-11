# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head):
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        n=len(l)
        for i in range(n):
            for j in range(i+1,n):
                if l[j]>l[i]:
                    l[i]=l[j]
                    break
            l[i]=0
        return l
#[2,1,5]#解答[5,5,0]#錯誤[0,0,0]
class Solution:
    def nextLargerNodes(self, head):
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        n=len(l)
        for i in range(n):
            m=l[i]
            l[i]=0
            for j in range(i+1,n):
                if l[j]>m:
                    l[i]=l[j]
                    break
        return l