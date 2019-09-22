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
        a=ListNode(val)
        p=head
        if head==None:
            return a
        while head and val>head.val:
            pre=head
            head=head.next
        pre.next=ListNode(val)
        pre.next.next=head
        return p