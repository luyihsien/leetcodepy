# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        b=head
        while head!=None:
            if (head.next).val==head.val:
                head.next=(head.next).next
                head=head.next
        return b
'''
AttributeError: 'NoneType' object has no attribute 'val'
Line 11 in deleteDuplicates (Solution.py)
'''