'''
219. Insert Node in Sorted Linked List
中文English
Insert a node in a sorted linked list.

样例
Example 1:

Input: head = 1->4->6->8->null, val = 5
Output: 1->4->5->6->8->null
Example 2:

Input: head = 1->null, val = 2
Output: 1->2->null
'''
#Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The head of linked list.
    @param val: An integer.
    @return: The head of new linked list.
    """
    def insertNode(self, head, val):
        if head==None:
            return ListNode(val)
        m=ListNode(0)
        m.next=head
        while head.val<val:
            if head.next==None:
                head.next=ListNode(val)
                return m.next
            if head.next.val>=val:
                n=head.next
                head.next=ListNode(val)
                head.next.next=n
                return m.next
            head=head.next
        a=ListNode(val)
        a.next=head
        return a